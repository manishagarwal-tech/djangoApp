from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import BlogPost
# Create your views here.

# import forms 
from .forms import BlogForm

def post_list_view(request):
    qs = BlogPost.objects.all().published()
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    template_name = 'blog.html'
    context = {'blog_lists': qs}
    return render(request, template_name, context)

@login_required
def post_create_view(request):
    form = BlogForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogForm()
    template_name = 'content/form.html'
    context = {
        'form': form,
        'page_title': 'Create Article'
    }
    return render(request, template_name, context)

@login_required
def post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'content/form.html'
    context = {'form':form, 'page_title': f"Updating {obj.title} ..." }
    return render(request, template_name, context)

@login_required
def post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'content/delete.html'
    if request.method == 'POST':
        obj.delete()
        return redirect("/blog")
    context = {'data': obj, }
    return render(request, template_name, context)

@login_required
def post_details_view(request, slug):
    try:
        obj = get_object_or_404(BlogPost, slug=slug)
        template_name = "content/details.html"
        context = {'blog': obj}
        return render(request, template_name, context)
    except Http404:
        return render(request, '404.html', status=404)