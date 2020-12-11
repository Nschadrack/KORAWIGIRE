from django import forms 
from . models import ContactMessage


# class ContactForm(forms.Form):
# 	full_name = forms.CharField(required=False, max_length=100, help_text='60 characters max.')
# 	email = forms.EmailField(required=False)
# 	subject = forms.CharField(required=False, max_length=100, help_text='100 characters max.')
# 	message = forms.CharField(required=True, widget=forms.Textarea)

class ContactForm(forms.ModelForm):
	full_name = forms.CharField(help_text='60 characters max.')
	email = forms.EmailField()
	subject = forms.CharField(help_text='100 characters max.')
	message = forms.CharField(widget=forms.Textarea)


	class Meta:
		model = ContactMessage
		fields = "__all__"
		exclude=['date_created']
