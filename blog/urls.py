from . import views
from django.urls import path
urlpatterns = [
    path("", views.index, name="blogHome"),
    path("blogpost", views.blogpost, name="blogPost")
]