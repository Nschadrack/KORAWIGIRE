import django_filters
from django_filters import CharFilter

from .models import *
from contact.models import ContactMessage

class PostFilter(django_filters.FilterSet):
	title = CharFilter(field_name='title', lookup_expr='icontains')
	class Meta:
		model = Post
		fields = []

class MessageFilter(django_filters.FilterSet):
	subject = CharFilter(field_name='subject', lookup_expr='icontains')
	class Meta:
		model = ContactMessage
		fields = []
		
