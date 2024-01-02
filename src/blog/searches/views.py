from django.shortcuts import render

from .models import SearchQuery
from blogAdmin.models import BlogPost

# Create your views here.
def search_view(request):
    query = request.GET.get('q', None)
    user = None
    if request.user.is_authenticated:
        user = request.user
    context = {'query': query}
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        blogList = BlogPost.objects.search(query=query)
        print(blogList)
        context['search_lists'] = blogList
    return render(request, 'view.html', context)