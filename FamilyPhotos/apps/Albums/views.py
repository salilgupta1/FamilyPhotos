from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

def home(request):
	return render(request,"Albums/index.html")