from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# import custom views
from .forms import *

def home_page(request):
    page_title = "Home"
    content = "this is a dummy content"
    return render(request, 'main.html', {'title':page_title, 'content':content})

def blog_footer(request):
    footer_text = 'Django Blogs'
    current_year = datetime.now().year
    template_name = 'components/footer.html'
    context = {'current_year' : current_year, 'footer_text':footer_text}
    return render(request, template_name, context)

def about_us(request):
    page_title = "About us"
    return render(request, 'about.html', {'title':page_title})

def contact(request):
    contact_form = ContactFrom(request.POST or None)
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    page_title = "Contact"
    context = {
        'title':page_title,
        'form' : contact_form
    }
    return render(request, 'contact.html', context)