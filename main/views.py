from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'main/index.html')


def language(request):
    return render(request,'main/language.html')

def project(request):
    return render(request,'main/project.html')
