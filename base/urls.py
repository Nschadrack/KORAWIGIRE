from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings 

  
app_name = 'base'


urlpatterns = [
    path('about/', views.about, name='about'),
    path('become_member/', views.becomeMember, name='become_member'),
    path('donate/', views.donate, name='donate'),
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)