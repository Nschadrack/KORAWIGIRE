# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from .models import *


# def post_user(sender, instance, created, **kwargs):

# 	if created:
# 		Post.objects.create(user=instance)

# post_save.connect(Post, sender=User)



# def post_image(sender, instance, created, **kwargs):
# 	if created:
# 		Post.objects.create(post_images=instance)

# post_save.connect(Post, sender=Post)