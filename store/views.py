from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

import json
import datetime

from decimal import Decimal
from .forms import OrderForm, CreateUserForm, ProductForm
from . utils import cartData, guestOrder
from .models import *

def RegisterPage(request):
    form = CreateUserForm()
    
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)
            
            return redirect('login')
    
    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def LoginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)   
        
        if user is not None:
            login(request, user)
            return redirect('store')
        else:
            messages.info(request,'Username or password is incorrect')
            return redirect(request,'login')
            
    context = {}
    return render(request, 'accounts/login.html', context)

def LogoutPage(request):
    logout(request)
    return redirect('store')

def ProfilePage(request):
    #Profile page
    #Add CRUD for name,username etc.
    data = cartData(request)
    
    cartItems = data['cartItems']
    context = {'cartItems': cartItems}
    
    return render(request, 'accounts/profile.html', context)

def get_search_results(query):
    if query:
        return Product.objects.filter(name__icontains=query)
    else:
        return Product.objects.all()

def get_filtered_results(min_price=None, max_price=None, queryset=None):
    if min_price is not None and max_price is not None:
        return queryset.filter(price__range=(min_price, max_price))
    elif min_price is not None:
        return queryset.filter(price__gte=min_price)
    elif max_price is not None:
        return queryset.filter(price__lte=max_price)
    else:
        return queryset

def search_filter(request):
    data = cartData(request)
    cartItems = data['cartItems']
    
    query = request.GET.get('q', '')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    
    min_price = Decimal(min_price) if min_price else None
    max_price = Decimal(max_price) if max_price else None
    
    search_results = get_search_results(query)
    results = get_filtered_results(min_price, max_price, search_results)
        
    context = {'results': results, 'cartItems': cartItems}
    
    return render(request, 'store/search.html', context)

def store(request):
    data = cartData(request)
    
    cartItems = data['cartItems']
    
    results = Product.objects.all()
    context = {'results': results, 'cartItems': cartItems}
    
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
        
        return JsonResponse('Item was added successfully', safe=False)
    
def AddProduct(request):
    
    data = cartData(request)
    
    cartItems = data['cartItems']
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            if 'image' in request.FILES:
                product.image = request.FILES['image']
            product.save()
            return redirect('store')
    else:
        form = ProductForm()
    
    context = {'cartItems': cartItems, 'form': form}
    return render(request, 'store/add_product.html', context)

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
        zipcode=data['shipping']['zipcode'],
        country=data['shipping']['country'],
        )
        
    return JsonResponse('Payment submitted..', safe=False)