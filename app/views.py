from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest
from django.shortcuts import render


def index(request):
    file_content = open('./contnets/index.html').read()
    content = {
        'content': file_content
    }
    return render(request,'base.html',content)
