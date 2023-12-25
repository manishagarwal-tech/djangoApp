from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def home_page(request):
    page_title = "Home"
    current_year = datetime.now().year
    return render(request, 'main.html', {'current_year' : current_year, 'title':page_title})


def about_us(request):
    page_title = "About us"
    return render(request, 'about.html', {'title':page_title})


def contact(request):
    page_title = "Contact"
    return render(request, 'contact.html', {'title':page_title})