#view.py
from django.shortcuts import render,redirect
from django.http import HttpResponse
#from django.contrib import messages
#from django.conf import settings
import random,os
#from app import forms
#from PLL import Image,ImageDraw,ImageFont
#from django.contrib.auth.decorators import login_required
from app import models
from .models import Post,upload_file
from datetime import datetime

# Create your views here.

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
		files = request.POST['file']
		print(files)
	except:
		files = request.POST['title']
	return render(request,'upload.html',locals())

def new(request):
	try:
		title = request.POST['title']
		body = request.POST['body']
	except:
		title = None
		message = "please enter block"
	
	post = models.Post.objects.create(title=title,slug=title,body=body)
	return render(request,'index.html',locals())

def create(request):
	return render(request,'new_post.html',locals())
