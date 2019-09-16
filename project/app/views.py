#view.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
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
        return redirect('/')

def posttest(request):
    post = Post.objects.all()
    return render(request,'test.html',locals())
