from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import BlogPost
# Create your views here.

def post_list_view(request):
    qs = BlogPost.objects.all()
    template_name = 'blog.html'
    context = {'blog_lists': qs}
    return render(request, template_name, context)

def post_create_view(request):
    template_name = 'content/create.html'
    context = {'form':None}
    return render(request, template_name, context)

def post_update_view(request):
    template_name = 'content/update.html'
    context = {'form':None}
    return render(request, template_name, context)

def post_delete_view(request):
    template_name = 'content/create.html'
    context = {'form':None}
    return render(request, template_name, context)

def post_details_view(request, slug):
    try:
        obj = get_object_or_404(BlogPost, slug=slug)
        template_name = "content/details.html"
        context = {'blog': obj}
        return render(request, template_name, context)
    except Http404:
        return render(request, '404.html', status=404)