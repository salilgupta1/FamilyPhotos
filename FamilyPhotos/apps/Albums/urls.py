from django.conf.urls import patterns, include, url
from FamilyPhotos.apps.Albums import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
	url(r'^createAlbum/$', views.createAlbum, name='createAlbum'),
	url(r'^allAlbums/$',views.viewAllAlbums, name='viewAllAlbums'),
	url(r'^album/(?P<albumuid>\d+)/$',views.viewAlbum, name='viewAlbum'),
)