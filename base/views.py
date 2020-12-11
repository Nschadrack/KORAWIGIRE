from django.shortcuts import render
from django.http import HttpResponse
from news.models import *


def home(request):
	latestnews=Post.objects.all().order_by('-date_created')
	posts=[]
	images=[]
	keep_im=[]
	numbers=[1,2,3,4]
	count=0
	title="Home"
	if latestnews:
		for num in range(len(latestnews)):
			if count<5:
				posts.append(latestnews[num])
				keep_im.append(posts[num].postimage_set.first())
				count+=1
			else:
				break

	if len(keep_im) != 0:
		first_image=keep_im[0]
		for image in range(1,len(keep_im)):
			images.append(keep_im[image])

		context = {'posts':posts, 'numbers':numbers, 'images':images, 'first_image':first_image, "title":title}
	else:
		context = {'posts':posts, 'numbers':numbers, 'images':images, "title":title}





	
	return render(request, 'home.html', context)



def about(request):

	context = {"title":"About Us"}
	return render(request, 'about.html', context)


def becomeMember(request):
	title="Become Member"
	context={"title":title}


	return render(request, 'become_member.html', context)



def donate(request):
	title="Donate"
	context={"title":title}


	return render(request, 'donate.html', context)