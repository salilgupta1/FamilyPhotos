from django.db import models

# Create your models here.
class Album(models.Model):
	title = models.CharField(max_length=150)
	description = models.CharField(max_length=300,blank=True, null=True)
	s3Location = models.FilePathField(path="/Albums/")
	timestamp = models.DateField(auto_now_add=True)
