from django.shortcuts import render
from .models import Product,Contact,Orders, OrderUpdate
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt



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
    thank = False
    if request.method == "POST":

        name = request.POST.get('name','')

        email =request.POST.get('email')
        phone =request.POST.get('phone')
        desc =request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True

    return render(request, 'shop/contact.html', {'thank': thank})


def Tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestap})
                    response = json.dumps([updates,order[0].item_json],default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/Tracker.html')


def Search(request):
    return render(request, 'shop/search.html')

def ProductView(request,myid):
    #fetch the product using id
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, 'shop/ProductView.html', {'product': product[0]})

def Checkout(request):
    if request.method == "POST":
        item_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(item_json=item_json, name=name, amount=amount,email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/Checkout.html', {'thank': thank, 'id': id})
        #request paytm to transfer amount from the user accounts
    return render(request, 'shop/Checkout.html')
@csrf_exempt
def handleRequest(request):
    #paytm will send you request
    pass