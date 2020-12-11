from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'news'

urlpatterns = [
    path('news/create/post/', views.create_post, name='create_post'),
    path('news/update/post<str:pk>/', views.update_post, name='update_post'),
    path('news/delete/post/<str:pk>/', views.before_delete, name='delete_post'),
    path('news/', views.posts, name='posts'),
    path('news/post/publish/<str:pk>/', views.post_publish, name='pub_post'),
    path('news/<str:title>/<str:pk>/on/<str:day>/<str:month>/<str:year>/', views.post_details, name='post_details'),
    path('news/<str:title>/<str:pk>/image/<str:id>/', views.full_image, name='single_image'),
    # path('news/<str:title>/<str:pk>/comment/<str:id>/image/<str:img_pk>/', views.full_image_comment, name='single_image_comment'),
    path('news/add/image/<str:pk>/', views.add_post_images, name='add_post_images'),
    path('news/delete/image/<str:pk>/', views.before_delete_image, name='delete_image'),
    

    ######################## COMMENT ##################################################

    path('news/post/<str:pk>/create/comment/', views.create_comment, name='create_comment'),
    # path('news/post/<str:pk>/update/comment<str:id>/', views.update_comment, name='update_comment'),
    path('news/post/delete/comment/<str:pk>/', views.before_delete_comment, name='delete_comment'),
    # path('news/post/<str:pk>/comments/', views.comments, name='comments'),


    ######################### ADMINISTRATION ##########################################
    
    path('dashboard/admin/', views.dashboard, name='dashboard'),
    path('dashboard/admin/post/<str:pk>/', views.post, name='admin_post'),
    path('dashboard/admin/post/<str:pk>/comment/<str:id>/', views.comment_view, name='admin_post_comment'),
    path('dashboard/admin/messages/', views.allMessage, name='allmessage'),
    path('dashboard/admin/message/<str:pk>/', views.singleMessage, name='singlemessage'),
    path('dashboard/admin/message/<str:pk>/delete/', views.delete_message, name='deletemessage'),
    

]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)