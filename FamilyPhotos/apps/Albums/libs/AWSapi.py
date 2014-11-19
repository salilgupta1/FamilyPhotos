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
		print bucket
		for image in files.getlist('photos'):
			k = Key(bucket)
			k.key = "%s/%s" % (object_name,image.name)
			k.set_contents_from_file(image)
			k.set_acl("public-read")
		end = time.time()
		return True
	except:
		print sys.exc_info()
		return False

def downloadPreviewsFromS3(keys):
	start = time.time()
	conn = connectToS3()
	try:
		bucket = conn.get_bucket(os.environ.get("S3_PHOTOS_BUCKET"))
		urls = []
		print keys
		for k in keys:
			prevImg = list(bucket.list(k.encode("utf-8"),"/*.*"))[0]
			url = prevImg.generate_url(expires_in=0, query_auth=False)
			urls.append(url)
		end = time.time()
		return urls
	except:
		print sys.exc_info()
		return []

def downloadAlbumFromS3(key):
	start = time.time()
	conn = connectToS3()
	try:
		bucket = conn.get_bucket(os.environ.get("S3_PHOTOS_BUCKET"))
		urls = []
		images = iter(bucket.list(key.encode("utf-8"),"/*.*"))
		for img in images:
			url = img.generate_url(expires_in=0,query_auth=False)
			urls.append(url)
		end = time.time()
		return urls
	except:
		print sys.exc_info()
		return []
	