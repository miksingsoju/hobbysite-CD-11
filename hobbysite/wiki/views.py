from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request, "homepage.html")

def article(request):
    return HttpResponse("Work in progress hehe")

def article_detail(request, num=1):
    return HttpResponse(f'Work in progress hehe: {num}')