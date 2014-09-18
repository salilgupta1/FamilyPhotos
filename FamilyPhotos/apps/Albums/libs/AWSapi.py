import boto
import os, sys
from boto.s3.key import Key
import time

def connectToS3():
	try:
		conn = boto.connect_s3()
		return conn
	except:
		print sys.exc_info()

def uploadToS3(files, object_name):
	start = time.time()
	conn = connectToS3()
	try:
		bucket = conn.get_bucket(os.environ.get("S3_PHOTOS_BUCKET"))
		for image in files.getlist('photos'):
			k = Key(bucket)
			k.key = "%s/%s" % (object_name,image.name)
			k.set_contents_from_file(image)
			k.set_acl("public_read")
		end = time.time()
	except:
		print sys.exc_info()
	print (end - start)

def downloadPreviewsFromS3(keys):
	start = time.time()
	conn = connectToS3()
	try:
		bucket = conn.get_bucket(os.environ.get("S3_PHOTOS_BUCKET"))
		urls = []
		for k in keys:
			prevImg = list(bucket.list(k.encode("utf-8"),"/*.*"))[0]
			imgName = prevImg.name.encode("utf-8").replace(" ","+")
			url = "https://s3-us-west-2.amazonaws.com/%s/%s" % (os.environ.get("S3_PHOTOS_BUCKET"), imgName)
			urls.append(url)
		end = time.time()
		print end - start
		return urls
	except:
		print sys.exc_info()

def downloadAlbumFromS3(key):
	start = time.time()
	conn = connectToS3()
	try:
		bucket = conn.get_bucket(os.environ.get("S3_PHOTOS_BUCKET"))
		urls = []
		images = iter(bucket.list(key.encode("utf-8"),"/*.*"))
		for img in images:
			imgName = img.name.encode("utf-8").replace(" ","+")
			url = "https://s3-us-west-2.amazonaws.com/%s/%s" % (os.environ.get("S3_PHOTOS_BUCKET"), imgName)
			urls.append(url)
		end = time.time()
		print end - start
		return urls
	except:
		print sys.exc_info()
	