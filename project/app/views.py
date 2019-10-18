#view.py
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
#from django.contrib import messages
#from django.conf import settings
import random,os
#from app import forms
#from PLL import Image,ImageDraw,ImageFont
#from django.contrib.auth.decorators import login_required
from app import models
from .models import Post,upload_file
from datetime import datetime
from django.conf import settings
from random import *
from django.views.decorators.csrf import csrf_exempt
from mqtt_test import mqtt_sub as sub

# Create your views here.
#---------------------------------------------
#mqtt
@csrf_exempt
def mqtt(request):
    #data = sub.getdata()
    data = sub.start()
    print(data)
#    sub.stop()
    return render(request,'CO2.html',locals())

#---------------------------------------------
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    #post_lists = list()
    #for count, post in enumerate(posts):
    #    post_lists.append("NO.{}:".format(str(count)) + str(post) +"<br>")
    #return HttpResponse(post_lists)
    return render(request,'index.html',locals())

def showpost(request, slug):
    print("12345")
    try:
        post = Post.objects.get(slug = slug)
        print("POST = " + str(post))
        if post != None:
            return render(request,'post.html',locals())
    except Exception as e:
        print(e)
        return redirect('/')

def posttest(request):
    post = Post.objects.all()
    return render(request,'test.html',locals())

def upload(request):
	try:
		files = request.FILES['test1']
#		path = os.path.realpath(files)
		save_path = '%s/%s'%(settings.MEDIA_ROOT,files.name)
		print(type(files.name))
#		print(save_path)
		with open(save_path, 'wb') as f:
			for chunk in files.chunks():
#				print(chunk)
				f.write(chunk)
		post = models.upload_file.objects.create(user_id=randint(0,25535),file_name=files.name,file_path=save_path)
	except Exception as e:
		print(e)
		print(1)
		files = request.POST['title']
		try:
			title = request.POST['title']
			body = request.POST['body']
		except:
			title = None
			message = "please enter block"
		post = models.Post.objects.create(title=title,slug=title,body=body)

	return render(request,'upload.html',locals())


def create(request):
	return render(request,'new_post.html',locals())

@csrf_exempt
def showth(request):
	return render(request,'show.html',locals())
