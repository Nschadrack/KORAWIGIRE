from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.contrib import messages



@unauthenticated_user
def loginPage(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('news:dashboard')
		else:
			messages.info(request, 'Username or Password is incorrect')

	return render(request, 'accounts/login.html')



@login_required(login_url='accounts:login')
def logoutUser(request):
	logout(request)
	return redirect('accounts:login')
