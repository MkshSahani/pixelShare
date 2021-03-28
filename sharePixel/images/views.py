from django.http.request import HttpRequest
from django.shortcuts import render

def home_page(request): 
    context = {}
    return render(request, 'images_base.html', context) # render home page.
