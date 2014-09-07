from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from forms import CreateAlbumForm
from uuid import uuid4
from django.core.context_processors import csrf
import os

# Create your views here.

def home(request):
	return render(request,"Albums/index.html")

def createAlbum(request):
	if request.method=="POST":
		form = CreateAlbumForm(request.POST, request.FILES)
		if form.is_valid():
			newAlbumForm=form.save(commit=False)
			S3_BUCKET = os.environ.get("S3_BUCKET")
			object_name = "Albums/%s" % (str(uuid4()))
			url ='https://%s.s3.amazonaws.com/%s' % (S3_BUCKET, object_name)
			tempForm.awsS3Storage = url
			newAlbumForm.save()
			#do the actual uploading of the images to amazon s3
	else:
		form = CreateAlbumForm()
	return render(request,"Albums/createAlbum.html",{"form":form})

def viewAllAlbums(request):
	pass

def viewAlbum(request):
	pass
