from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from forms import CreateAlbumForm
from uuid import uuid4
from django.core.context_processors import csrf
from libs.AWSapi import uploadToS3
# Create your views here.

def home(request):
	return render(request,"Albums/index.html")

def createAlbum(request):
	if request.method=="POST":
		form = CreateAlbumForm(request.POST, request.FILES)
		if form.is_valid():
			newAlbumForm=form.save(commit=False)
			object_name = "Albums/%s" % (str(uuid4()))
			newAlbumForm.awsObjectName = object_name
			newAlbumForm.save()
			uploadToS3(request.FILES,object_name)
			return render(request,"Albums/createAlbum.html",{"Success":"Success"})
	else:
		form = CreateAlbumForm()
		return render(request,"Albums/createAlbum.html",{"form":form})

def viewAllAlbums(request):
	pass

def viewAlbum(request):
	pass
