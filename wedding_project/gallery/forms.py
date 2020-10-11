from django import forms 
from .models import *

class UploadPictureForm(forms.ModelForm): 

	class Meta: 
		model = Picture 
		fields = ['picture'] 
