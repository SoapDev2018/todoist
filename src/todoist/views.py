from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

def home_page(request):
    template_name = 'home.html'
    context = {
        "title": "A Todos App"
    }
    return render(request, template_name, context=context)

def about_page(request):
    template_name = "about.html"
    context = {
        "title": "About Us"
    }
    return render(request, template_name, context=context)