from django.http import HttpResponse 
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from azure.storage.blob import BlockBlobService
from .forms import *


def upload_picture_view(request): 

	if request.method == 'POST': 
		form = UploadPictureForm(request.POST, request.FILES) 

		if form.is_valid(): 
			form.save() 
			return redirect('display_gallery') 
	else: 
		form = UploadPictureForm() 
	return render(request, 'picture_upload.html', {'form' : form}) 

def display_gallery(request): 
	pictures = Picture.objects.filter(is_approved=True)
	isEmpty = pictures.exists() 
	return render(request, 'display_gallery.html', {'pictures': pictures, 'isEmpty':isEmpty}) 

def display_gallery_toapprove(request):
	if request.user.is_authenticated:
		Pictures = Picture.objects.all() 
		length = Picture.objects.filter(is_approved=False).count()
		
		return render(request, 'display_gallery_toapprove.html', {'pictures': Pictures, 'length':length}) 
	else:
		return redirect('login')

def approve_picture(request, pk):

	picture = Picture.objects.get(pk=pk)

	pic_form = UploadPictureForm(request.POST, instance=picture)

	if pic_form.is_valid():
		picture = pic_form.save(commit=False)
		picture.is_approved = True
	 
		picture.save()
	
	return redirect('display_gallery_toapprove')

def delete_picture(request, pk):
	pic = Picture.objects.get(pk=pk)

	block_blob_service = BlockBlobService(account_name='djangodemo', account_key='wHisO/rq7ZD5FgKETqdPFWDraDdyVIveAFRW/TpZnHJ0t1KjNJcP9mOvMS9cIDX+QHBOMLVgXlUXft+QHrp1eA==')
	block_blob_service.delete_blob('media', '{}'.format(pic.picture))
	
	Picture.objects.filter(pk=pk).delete()
	
	return redirect('display_gallery_toapprove')

def logout_view(request):
	logout(request)
	
	return redirect('display_gallery')