from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import *

urlpatterns = [
	path('', display_gallery, name = 'display_gallery'),
	path('logout', logout_view, name = 'logout_view'),
    path('approve_picture/<int:pk>/', approve_picture, name='approve_picture'),
	path('delete_picture/<int:pk>/', delete_picture, name='delete_picture'),
	path('approve_picture/', display_gallery_toapprove, name='display_gallery_toapprove'),
    path('image_upload', upload_picture_view, name = 'picture_upload'), 
    path('display_gallery', display_gallery, name = 'display_gallery'),
]