from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings 

from .forms import ContactForm
from .models import ContactMessage

# Create your views here.

def contact(request):
	title='Contact Us Here'
	title_head="Contact Us"
	confirm_message=None
	form = ContactForm()
	if request.method == "POST":
		form = ContactForm(request.POST or None)
		if form.is_valid():
			name = form.cleaned_data['full_name']
			message = form.cleaned_data['message']
			subject = form.cleaned_data['subject']
			emailFrom = form.cleaned_data['email']
			emailTo = [settings.EMAIL_HOST_USER]

			form.save()

			send_mail(subject, message, emailFrom, emailTo, fail_silently=False)

			title='Thanks!'
			confirm_message='Thanks for the message. We will get right back to you'
			form = None
			
	context={'title':title, 'form':form, 
	'confirm_message':confirm_message,
	"title_head":title_head}
	template = 'contact.html'
	return render(request, template, context)

