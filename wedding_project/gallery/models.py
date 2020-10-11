from django.db import models

class Picture(models.Model):
	picture = models.ImageField(null=False, blank=False, upload_to="images/")
	is_approved = models.BooleanField(default=False)
