"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# import all views to setup url path
from .views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
# import views from blog-admin app
from blogAdmin.views import post_list_view 
from searches.views import search_view
urlpatterns = [
    # url for admin area
    path('wp-admin/', admin.site.urls),
    # include the blog urls
    path('blog/', include('blogAdmin.urls')),
    # urls for front-end areas
    path('', home_page, name="home"),
    path('about/', about_us, name="about"),
    path('contact/', contact, name="contact"),
    path('blog/', post_list_view, name="blogs"),
    path('search/', search_view, name="search"),
    path('logout/', LogoutView.as_view(), name="logout"),
    
]

if settings.DEBUG:
    #test mode-> view the media files
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
