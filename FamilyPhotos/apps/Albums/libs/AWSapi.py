import boto
import os, sys
from boto.s3.key import Key
import time

def connectToS3():
	try:
		conn = boto.connect_s3(os.environ.get("AWS_ACCESS_KEY"),os.environ.get("AWS_SECRET_KEY"))
		return conn
	except:
		print sys.exc_info()[0]

def uploadToS3(files, object_name):
	start = time.time()
	conn = connectToS3()
	try:
		bucket = conn.get_bucket(os.environ.get("S3_BUCKET"))
		for image in files.getlist('photos'):
			k = Key(bucket)
			k.key = "%s/%s" % (object_name,image.name)
			k.set_contents_from_file(image)
		end = time.time()
	except:
		print sys.exc_info()
	print (end - start)

def downloadFromS3():
	pass