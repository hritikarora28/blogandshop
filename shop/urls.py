from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="shophome"),
    path("About", views.About, name="About US"),
    path("Contact", views.contact, name="Contact us"),
    path("Tracker", views.Tracker, name="Tracing Status"),
    path("Search", views.Search, name="Search"),
    path("products/<int:myid>", views.ProductView, name="Product View"),
    path("Checkout", views.Checkout, name="Checkout"),
    path("handleRequest", views.handleRequest, name="HandleRequest"),

]