import json
from .models import *


def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    print('Cart:', cart)
    items = []
    order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
    cartItems = order['get_cart_items']
    
    for i in cart:
        try:
            cartItems += cart[i]["quantity"]
            
            product =  Product.objects.get(id=i)
            total = (product.price * cart[i]["quantity"])
            
            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]["quantity"]
            
            item ={
                'product' :{
                    'id':product.id,
                    'product':product.name,
                    'price':product.price,
                    'imageURL':product.imageURL,
                },
                'quantity':cart[i]["quantity"],
                'get_total':total
            }
            items.append(item)
            
            order['shipping'] = True
        except:
            pass
    return{'cartItems':cartItems, 'order':order, 'items':items}

def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items =  order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
    return{'cartItems':cartItems, 'order':order, 'items':items}

def guestOrder(request, data):
	name = data['form']['name']
	email = data['form']['email']

	cookieData = cookieCart(request)
	items = cookieData['items']

	customer, created = Customer.objects.get_or_create(
			email=email,
			)
	customer.name = name
	customer.save()

	order = Order.objects.create(
		customer=customer,
		complete=False,
		)

	for item in items:
		product = Product.objects.get(id=item['product']['id'])
		orderItem = OrderItem.objects.create(
			product=product,
			order=order,
			quantity=item['quantity'],
		)
	return customer, order

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