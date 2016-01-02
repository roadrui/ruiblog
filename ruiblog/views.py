
# Create your views here.
from django.shortcuts import render
from ruiblog.models import BlogsPost
from django.shortcuts import render_to_response

def index(request):
    print('ok excute')
    blog_list = BlogsPost.objects.all()
    return render_to_response('index.html',{'blog_list':blog_list})

def register(request):
    return render_to_response('register.html',{})

def login(request):
    return render_to_response('login.html',{})
