from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest
from django.shortcuts import render

pages = [
    {
        'url':'/',
        'title': 'Home',
    },
    {
        'url':'/about',
        'title': 'About',
    },
    {
        'url':'/projects',
        'title': 'Projects',
    },
    {
        'url':'/contact',
        'title': 'Contact',
    }
]

def index(request):
    file_content = open('./app/contents/index.html').read()
    content = {
        'content': file_content,
        'pages': pages,
        'title': 'Home'
    }
    return render(request,'app/base.html',content)
def about(request):
    file_content = open('./app/contents/about.html').read()
    content = {
        'content': file_content,
        'pages': pages,
        'title': 'About'
    }
    return render(request,'app/base.html',content)

def projects(request):
    file_content = open('./app/contents/projects.html').read()
    content = {
        'content': file_content,
        'pages': pages,
        'title': 'Projects'
    }
    return render(request,'app/base.html',content)

def contact(request):
    file_content = open('./app/contents/contact.html').read()
    content = {
        'content': file_content,
        'pages': pages,
        'title': 'Contact'
    }
    return render(request,'app/base.html',content)