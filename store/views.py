from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *
from .utils import cookieCart, cartData, guestOrder
from .forms import sign_in,sign_up
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def store(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()
    context = {'products':products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)

def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

# from django.views.decorators.csrf import csrf_exempt
#
# @csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment complete!', safe=False)

def log_in(request):
    if request.method=="POST":
        fillform = sign_in(request.POST)
        if(fillform.is_valid()):
            user_name= fillform.cleaned_data["Username"]
            password = fillform.cleaned_data["Password"]
            SignIn = authenticate(request, username=user_name,password=password)
            if SignIn is not None :

                login(request,SignIn)
                return redirect('/')
            else:
                fillform = sign_in()
                message='Invalid username, Please Try again'
                return render(request,'store/login.html',{'form':fillform,'message':message})
    else:
        fillform=sign_in()
        return render(request,'store/login.html',{'form':fillform})

def signup(request):
    if request.method =="POST":
        fillform= sign_up(request.POST)
        if (fillform.is_valid()):
            user_name =fillform.cleaned_data["username"]
            email = fillform.cleaned_data["email"]
            password = fillform.cleaned_data["password"]
            first_name1= fillform.cleaned_data["Firstname"]
            last_name1 = fillform.cleaned_data["Lastname"]
            try:
                User.objects.get(username=user_name)
                return redirect("/signup/")
            except:
                x= User.objects.create_user(user_name,email,password)
                x.last_name =last_name1
                x.first_name =first_name1
                x.save()
                SignIn = authenticate(request, username=user_name,password=password)
                login(request,SignIn)

                y= Customer.objects.create(user=request.user,name=first_name1)
                y.save()
                print(y)
                return redirect('/')
    else:
        fillform=sign_up()
        return render(request,'store/signup.html',{'form':fillform})
        
def signout(request):
    logout(request)
    return redirect('/')
