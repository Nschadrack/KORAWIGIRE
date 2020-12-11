from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from contact.models import ContactMessage
from .forms import PostForm, PostFormImage,CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .filters import PostFilter,MessageFilter
from django.core.paginator import Paginator





#################################### ADMIN CREATING A POST #####################################################
@login_required(login_url='accounts:login')
def create_post(request):
	user=request.user
	message="Create a New Post"
	create=True
	form = PostForm()
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.user=user
			post.save()
			post=Post.objects.last()
			print("POST_ID: ", post.id)
			
			# print("POST.USER: ", post.user)
			
			return redirect('news:add_post_images', pk=post.id)

			
	context={'form':form, 'message':message, 'create':create, "title":"Create New Post"}
	return render(request, 'news/create_post.html', context)






############################ Adding Images To The Post ################################################
@login_required(login_url='accounts:login')
def add_post_images(request, pk):
	post = Post.objects.get(id=pk)
	form = PostFormImage()
	another=False
	if request.method == "POST":
		form = PostFormImage(request.POST, request.FILES)
		if form.is_valid():
			image=form.save(commit=False)
			image.post_images=post
			image.save()
			another=True
			context={'form':form, 'True':another, 'post':post, "title":"Add Images To Post"}
			return render(request, 'news/create_image.html', context)

	context={'form':form,'True':another, 'post':post, "title":"Add Images To Post"}
	return render(request, 'news/create_image.html', context)




############################## Making POST TO BE VIEWED PUBLICLY #####################################
def post_publish(request, pk):
	post=Post.objects.get(id=pk)
	post.publish()
	return redirect('news:posts')






############################# UPDATING POST ##########################################################
def update_post(request, pk):
	post=Post.objects.get(id=pk)
	updating=True
	message="Update Post"
	form=PostForm(instance=post)
	if request.method == "POST":
		form=PostForm(request.POST, instance=post)
		if form.is_valid():
			form.save()
			return redirect('news:admin_post', post.id)

	context={"form":form, "updating":updating, "message":message, "title":"Update Post" }
	return render(request, 'news/create_post.html', context)





############################### DELETING A POST #######################################################
@login_required(login_url="accounts:login")
def before_delete(request, pk):
	post_message="Do you really want to delete this post?"
	comment_message=None
	post_image=None
	if request.method == 'POST':
		def delete_post(request):
			post=Post.objects.get(id=pk)
			post.delete()
			return redirect('news:dashboard')
		return delete_post(request)
	context={"post_message":post_message, "comment_message":comment_message, "title":"Delete Post"}
	return render(request, 'news/delete_post.html', context)


@login_required(login_url='accounts:login')
def before_delete_image(request, pk):
	post_image="Do you really want to delete this image?"
	post_message=None
	comment_message=None
	if request.method == 'POST':
		def delete_post(request):
			post=Post.objects.get(id=pk)
			post.delete()
			return redirect('news:dashboard')
		return delete_post(request)
	context={"post_message":post_message, 
			"comment_message":comment_message,
			"post_image":post_image,
			"title":"Delete Image"}
	return render(request, 'news/delete_post.html', context)






#################################### LIST OF ALL POST #######################################################
def posts(request):
	posts_list = Post.objects.all().order_by('-date_created')
	paginator = Paginator(posts_list, 8)
	page_number = request.GET.get('page')
	posts = paginator.get_page(page_number)
	
	context={'posts':posts, "title":"News Page"}
	return render(request, 'news/posts_list.html', context)





##################################### Viewing full details for each post #####################################
def post_details(request, pk, title, day, month, year):
	post = Post.objects.get(id=pk)
	context={'post': post, "title":"Post Details"}
	return render(request, 'news/post_details.html', context)






###################################### Creating comment for each post ##########################################
def create_comment(request, pk):
	post = Post.objects.get(pk=pk)
	form = CommentForm()
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment=form.save(commit=False)
			comment.post=post
			comment.save()
			return redirect('news:post_details', 
				title=post.title, pk=post.id,
				day=post.date_created.day,
				month=post.date_created.month,
				year=post.date_created.year)
		else:
			print("\n\n")
			for error in form.errors:
				print("Form error: ", error)
				print("\n")
	context={"form":form, "title":"Create Comment"}

	return render(request, 'news/comment_form.html', context)






############################# Viewing Full each Image ##################################################

def full_image(request, pk, id, title):
	post = Post.objects.get(id=pk)
	image=post.postimage_set.get(id=id)

	context={'image': image}
	return render(request, 'news/full_image.html', context)



@login_required(login_url='accounts:login')
def before_delete_image(request, pk):
	image=PostImage.objects.get(id=pk)
	keep=image.post_images.id
	post_image="Do you really want to delete this image?"
	post_message=None
	comment_message=None
	if request.method == 'POST':
		def delete_post(request):
			image.delete()
			return redirect('news:admin_post', keep)
		return delete_post(request)
	context={"post_message":post_message,
			"comment_message":comment_message,
			"post_image":post_image,
			'keep':keep}
	return render(request, 'news/delete_post.html', context)



################################ Admin Deleting a single Comment for each single post #####################
def before_delete_comment(request, pk):
	post_message=None
	post_image=None
	comment=Comment.objects.get(id=pk)
	keep=comment.post.id
	comment_message="Do you really want to delete this comment?"
	if request.method == 'POST':
		def delete_comment(request):
			comment.delete()
			return redirect('news:admin_post', keep)
		return delete_comment(request)
	context={"post_message":post_message, "comment_message":comment_message, "keep":keep}
	return render(request, 'news/delete_post.html', context)





######################### ADMINISTRATION PART VIEWS ###################

@login_required(login_url='accounts:login')
def dashboard(request):
	posts = Post.objects.all().order_by('-date_created')
	comments = Comment.objects.all().order_by('-date_created')
	myFilter=PostFilter(request.GET, queryset=posts)
	posts=myFilter.qs

	context={'posts':posts, 'comments':comments, "myFilter":myFilter}
	return render(request, 'kofaob_admin/dashboard.html', context)






######################### Admin Viewing a single Post ###########################################
@login_required(login_url='accounts:login')
def post(request, pk):
	post = Post.objects.get(id=pk)
	context={'post': post}
	return render(request, 'kofaob_admin/post.html', context)






########################## Admin Viewing a single Comment for each post #########################
@login_required(login_url='accounts:login')
def comment_view(request, pk, id):
	post = Post.objects.get(id=pk)
	comment=post.comment_set.get(id=id)
	context={'post': post, 'comment':comment}
	return render(request, 'kofaob_admin/comment_detail.html', context)



########################## CONTACT MESSAGE ADMIN ############################

@login_required(login_url='accounts:login')
def allMessage(request):
	contact_messages = ContactMessage.objects.all()
	myFilter=MessageFilter(request.GET, queryset=contact_messages)
	contact_messages=myFilter.qs


	context={'contact_messages':contact_messages, "myFilter":myFilter}
	return render(request, 'kofaob_admin/messages.html', context)


def singleMessage(request, pk):
	message = ContactMessage.objects.get(id=pk)


	context={'message':message}
	return render(request, 'kofaob_admin/message_detail.html', context)

def delete_message(request, pk):

	try:
		message=ContactMessage.objects.get(id=pk)
		message.delete()
		messages.success(request,"Message has been deleted successfully!!")
		return redirect('news:allmessage')
	except ContactMessage.DoesNotExist:
		messages.success(request,"Message has been deleted unsuccessfully!!")
		return redirect('news:allmessage')

	


