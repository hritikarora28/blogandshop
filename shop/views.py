from django.shortcuts import render
from .models import Product,Contact
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
    if request.method == "POST":
        print(request)
        name = request.POST.get('name','')

        email =request.POST.get('email')
        phone =request.POST.get('phone')
        desc =request.POST.get('desc')
        contact = Contact(name =name, email=email, phone=phone, desc=desc)
        contact.save()

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