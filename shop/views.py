from django.shortcuts import render
from .models import Product
from math import ceil

# Create your views here.
from django.http import HttpResponse

def index(request):
    #products = Product.objects.all()
    #n = len(products)
    #nSlides = n//4 + ceil((n/4)-(n//4))
    #allProds = [[products, range(1, len(products)), nSlides],[products, range(1, len(products)), nSlides]]
    allProds =[]
    catprod = Product.objects.values('product_catergory', 'id')
    cats = {item['product_catergory'] for item in catprod}
    for cat in cats:
        prod = Product.objects.filter(product_catergory=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, len(prod)), nSlides])
    params = {'allProds':allProds }

    return render(request,"shop/index.html", params)

def About(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def Tracker(request):
    return render(request, 'shop/Tracker.html')

def Search(request):
    return render(request, 'shop/search.html')

def ProductView(request,myid):
    #fetch the product using id
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, 'shop/ProductView.html', {'product': product[0]})

def Checkout(request):
    return render(request, 'shop/Checkout.html')