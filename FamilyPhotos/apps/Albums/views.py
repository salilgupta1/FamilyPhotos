from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from forms import CreateAlbumForm
from django.core.context_processors import csrf

# Create your views here.

def home(request):
	return render(request,"Albums/index.html")

def createAlbum(request):
	if request.method == "POST":
		form = CreateAlbumForm(request.POST, request.FILES)
	else:
		form = CreateAlbumForm()
	return render(request,"Albums/createAlbum.html",{"form":form})

def viewAllAlbums(request):
	pass

def viewAlbum(request):
	pass
