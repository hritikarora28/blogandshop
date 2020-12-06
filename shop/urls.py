from . import views
from django.urls import path

urlpatterns = [
    path("Home", views.index, name="shophome"),
    path("About", views.About, name="About US"),
    path("Contact", views.contact, name="Contact us"),
    path("Tracer", views.Tracker, name="Tracing Status"),
    path("Search", views.Search, name="Search"),
    path("ProductView", views.ProductView, name="Product View"),
    path("Checkout", views.Checkout, name="Checkout"),

]