import boto
import os, sys
from boto.s3.key import Key
import time
import threading

def connectToS3():
	try:
		conn = boto.connect_s3()
		return conn
	except:
		print sys.exc_info()

def uploadToS3(files, object_name):
	numFiles = len(files.getlist('photos'))

	# use a max of 10 threads otherwise 
	numThreads = numFiles if numFiles < 10 else 10

	try:
		# if numThreads less than max then just use 1 thread per image
		if numThreads == numFiles:
			for i in range(numThreads):
				img = [files.getlist('photos')[i]]
				t = threading.Thread(target=upload, args=(img,object_name,)).start()

		# if numThreads = 10 split images between 10 threads
		else:
			numFilesPerThread = numFiles/numThreads
			remainder = numFiles % numThreads
			end = 0
			start = 0
			while start < numFiles:
				# distribute images
				if remainder:
					end = end + numFilesPerThread + 1
					remainder -=1
				else:
					end = end + numFilesPerThread
				imgs = files.getlist('photos')[start:end]

				start = end
				# allocate each thread a portion of the images
				t = threading.Thread(target=upload,args=(imgs,object_name,)).start()
	except:
		print sys.exc_info()
		return False
	return True

def upload(images,obj_name):
	conn = connectToS3()
	bucket = conn.get_bucket(os.environ.get("S3_PHOTOS_BUCKET"))
	for image in images:	
		k = Key(bucket)
		k.key = "%s/%s" % (obj_name,image.name)
		k.set_contents_from_file(image)
		k.set_acl("public-read")
	return True

def downloadPreviewsFromS3(keys):
	conn = connectToS3()
	try:
		bucket = conn.get_bucket(os.environ.get("S3_PHOTOS_BUCKET"))
		urlsWithKeys = []
		for k in keys:
			try:
				# necessary in order to deal with orphan rows in the db
				prevImg = list(bucket.list(k.encode("utf-8"),"/*.*"))[0]
				url = prevImg.generate_url(expires_in=0, query_auth=False)
				urlsWithKeys.append((url,k))
			except IndexError:
				print sys.exc_info()
				continue
		return urlsWithKeys
	except:
		print sys.exc_info()
		return []

def downloadAlbumFromS3(key):
	conn = connectToS3()
	try:
		bucket = conn.get_bucket(os.environ.get("S3_PHOTOS_BUCKET"))
		urls = []
		images = iter(bucket.list(key.encode("utf-8"),"/*.*"))
		for img in images:
			url = img.generate_url(expires_in=0,query_auth=False)
			urls.append(url)
		return urls
	except:
		print sys.exc_info()
		return []
	