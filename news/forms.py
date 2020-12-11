from django.forms import ModelForm, CharField, Textarea
from .models import*



class PostForm(ModelForm):

	class Meta:
		model = Post 

		fields = '__all__'
		exclude = ['date_created', 'publish_post', 'user']



class PostFormImage(ModelForm):
	class Meta:
		model = PostImage 

		fields = '__all__'
		exclude=['post_images']


class CommentForm(ModelForm):
	author = CharField(label='Full Name')
	body = CharField(label='Your Comment', widget=Textarea(), required=True)
	class Meta:
		model = Comment 
		fields = '__all__'
		exclude=['date_created', 'post']


