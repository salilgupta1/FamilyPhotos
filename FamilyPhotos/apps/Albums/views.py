from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from forms import CreateAlbumForm
from models import *
from uuid import uuid4
from django.core.context_processors import csrf
from libs.AWSapi import *
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
			success = uploadToS3(request.FILES,object_name)
			if success:
				newAlbumForm.save()
				return render(request,"Albums/createAlbum.html",{"Success":"Congratulations Dad! You Uploaded an album!"})
			else:
				return render(request,"Albums/createAlbum.html",{"Error":"Uh oh something bad happened!"})
	else:
		form = CreateAlbumForm()
	return render(request,"Albums/createAlbum.html",{"form":form})

def viewAllAlbums(request):
	albums = Album.objects.all()
	if albums:
		keys = [k.awsObjectName for k in albums]
		albumUIDS = [k.albumUID for k in albums]
		urls = downloadPreviewsFromS3(keys)
		if len(urls):
			previewPhotos = zip(downloadPreviewsFromS3(keys),albumUIDS)
			return render(request, "Albums/viewImages.html", {"previewPhotos":previewPhotos})	
	return render(request, "Albums/viewImages.html",{"empty":"Dad you haven't added any albums yet!"})

def viewAlbum(request,albumuid):
	album = Album.objects.get(albumUID=albumuid)
	key = album.awsObjectName
	metadata = {"title":album.title, "description":album.description}
	images = downloadAlbumFromS3(key)
	return render(request, "Albums/viewImages.html",{"images":images,"metadata":metadata})

	
