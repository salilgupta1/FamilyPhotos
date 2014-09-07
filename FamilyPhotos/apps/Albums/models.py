from django.db import models

# Create your models here.
class Album(models.Model):
	title = models.CharField(max_length=150)
	albumUID = models.AutoField(primary_key=True)
	description = models.CharField(max_length=300,blank=True, null=True)
	awsS3Storage = models.URLField(max_length=400)
	timestamp = models.DateField(auto_now_add=True)
