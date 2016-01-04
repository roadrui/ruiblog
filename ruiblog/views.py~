
# Create your views here.
from django.shortcuts import render
from ruiblog.models import BlogsPost
from django.shortcuts import render_to_response
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
def index(request):
    blogs = BlogsPost.objects.all()
    page = request.GET.get('page')
    blog_list = pages(blogs,page,3)
    return render_to_response('index.html',{'blog_list':blog_list})


def pages(datas,page,num):
    paginator = Paginator(datas,num)
    try:
        data_list = paginator.page(page)
    except PageNotAnInteger:
        data_list = paginator.page(1)
    except EmptyPage:
        data_list = paginator.paginator(paginator.num_pages)
    return data_list
'''
def register(request):
    return render_to_response('register.html',{})

def login(request):
    return render_to_response('login.html',{})

def registerapi(request):
    print("it's have been execute") 
    return render_to_response('login.html',{})
'''
def detail(request,pk):
    try:
        print('hello')
        blog = BlogsPost.objects.get(pk=pk)
        summary = blog.body.__str__()
        summ = summary[0:5]
        print(summ)
    except BlogsPost.DoesNotExist:
        raise Http404
    return render(request,'blog.html',{'blog':blog})
   
def about_me(request):
    return render(request,'aboutme.html')


def blog_search(request):
    if 'searchKey' in request.GET:
        keyword = request.GET['searchKey']
        if not keyword :
                return render(request,'index.html',{'error':True})
        else:
            blog_list = BlogsPost.objects.filter(title__icontains = keyword)
            if len(blog_list)==0 :
                print('it error')
                return render(request,'index.html',{'blog_list':blog_list,'error':True})
            else:
                print('it ok')
                return render(request,'index.html',{'blog_list':blog_list,'error':False})
    return redirect('/')

















