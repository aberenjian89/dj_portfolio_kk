from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest
from django.shortcuts import render
import requests

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
    # file_content = open('./app/index.html').read()
    content = {
        # 'content': file_content,
        'pages': pages,
        'title': 'Home'
    }
    return render(request,'app/index.html',content)
def about(request):
    # file_content = open('./app/contents/about.html').read()
    content = {
        # 'content': file_content,
        'pages': pages,
        'title': 'About'
    }
    return render(request,'app/about.html',content)

def projects(request):
    response = requests.get('https://api.github.com/users/aberenjian89/repos')
    repos = response.json
    print(repos)
    # file_content = open('./app/contents/projects.html').read()
    content = {
        # 'content': file_content,
        'pages': pages,
        'repos': repos,
        'title': 'Projects'
    }
    return render(request,'app/projects.html',content)

def contact(request):
    # file_content = open('./app/contents/contact.html').read()
    content = {
        # 'content': file_content,
        'pages': pages,
        'title': 'Contact'
    }
    return render(request,'app/contact.html',content)