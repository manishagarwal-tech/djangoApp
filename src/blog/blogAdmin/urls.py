from django.urls import path
# import all views to setup url path
from .views import *
from django.contrib.auth.views import LogoutView

# import views from blog-admin app
from .views import * 

urlpatterns = [
    # urls for front-end areas
    path('new', post_create_view, name="create"),
    path('<str:slug>/', post_details_view, name='post_details'),
    path('<str:slug>/update', post_update_view, name="update"),
    path('<str:slug>/delete', post_delete_view, name="delete"),
]
