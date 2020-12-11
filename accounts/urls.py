from django.urls import path 
from .import views

app_name='accounts'

urlpatterns = [
	path("login/", views.loginPage, name='login'),
	path("logout/", views.logoutUser, name='logout'),
	]