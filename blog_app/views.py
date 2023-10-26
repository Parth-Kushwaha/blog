from django.shortcuts import render

from .models import Post

# Create your views here.

def home(request):
    posts=Post.objects.all()
    
    context={
        'posts': posts
    }
    return render(request, 'blog_app/home.html',context)

def about(request):
    context={
        'title':'About'
    }
    return render(request, 'blog_app/about.html', context)