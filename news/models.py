from datetime import datetime
from django.db import models
from django.contrib.auth.models import User




class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
	title = models.CharField(null=True, max_length=100)
	body = models.TextField(null=True)
	date_created = models.DateTimeField(null=True, default=datetime.utcnow)
	publish_post = models.BooleanField(default=False, null=True)


	def publish(self):
		self.publish_post=True
		self.save()



	def return_title(self):
		return self.title




	def comments(self):

		post_comments = self.comment_set.all()

		return post_comments.count()



	def __str__(self):
		return self.title


class Comment(models.Model):
	post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, blank=True)
	author = models.CharField(null=True, max_length=40)
	body = models.TextField(null=True)
	date_created = models.DateTimeField(default=datetime.utcnow)


	def __str__(self):
		return self.body




class PostImage(models.Model):
	post_images = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, blank=True)
	image_filename = models.ImageField(null=True, upload_to='news/images/post')
	description = models.CharField(null=True, max_length=60, blank=True)


