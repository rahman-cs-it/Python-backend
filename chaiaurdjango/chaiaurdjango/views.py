from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello world , you are at my home page")
    return render(request,'index.html',{'name': 'Home'})

def about(request):
    # return HttpResponse("Hello world , you are at my about page")
    return render(request,'index.html',{'name': 'About'})

def contact(request):
    # return HttpResponse("Hello world , you are at my contact page")
    return render(request,'index.html',{'name': 'Contact'})