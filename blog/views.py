from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'NiteshSBlog',
        'title': 'Blog Post 1',
        'comment': 'First post content',
        'date_posted': 'August_21'
    },

       {
        'author': 'BGSBlog',
        'title': 'Blog Post 2',
        'comment': 'Second post content',
        'date_posted': 'August_28'
    },
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})