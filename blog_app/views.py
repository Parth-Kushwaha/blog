from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

def home(request):
    posts=Post.objects.all()
    
    context={
        'posts': posts
    }
    return render(request, 'blog_app/home.html',context)

class PostListView(ListView):
    model= Post
    template_name= 'blog_app/home.html'
    context_object_name= 'posts'
    ordering=['-date_posted']

class PostDetailView(DetailView):
    model= Post


def about(request):
    context={
        'title':'About'
    }
    return render(request, 'blog_app/about.html', context)