from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'shop/index.html')
def About(request):
    return HttpResponse("we are at about")
def contact(request):
    return HttpResponse("we are at contact")
def Tracker(request):
    return HttpResponse("we are at tracker")
def Search(request):
    return HttpResponse("we are at search")
def ProductView(request):
    return  HttpResponse("we are at product View")
def Checkout(request):
    return  HttpResponse("we are at checkout")