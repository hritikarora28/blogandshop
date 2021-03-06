from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="shophome"),
    path("About", views.About, name="About US"),
    path("Contact", views.contact, name="Contact us"),
    path("Tracker", views.Tracker, name="Tracing Status"),
    path("search", views.search, name="search"),
    path("products/<int:myid>", views.ProductView, name="Product View"),
    path("Checkout", views.Checkout, name="Checkout"),
    path("handlerequest", views.handlerequest, name="HandleRequest"),

]