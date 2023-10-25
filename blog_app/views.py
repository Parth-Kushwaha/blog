from django.shortcuts import render

# Create your views here.

posts=[
    {
        'title':'Blog-1 Title',
        'author':'Parth Kushwaha',
        'content':'This is blog-1 content',
        'date_posted':'25-10-23'
    },
    {
        'title':'Blog-2 Title',
        'author':'Disha Sharma',
        'content':'This is blog-2 content',
        'date_posted':'26-10-23'
    },
]

def home(request):
    context={
        'posts':posts
    }
    return render(request, 'blog_app/home.html',context)

def about(request):
    context={
        'title':'About'
    }
    return render(request, 'blog_app/about.html', context)