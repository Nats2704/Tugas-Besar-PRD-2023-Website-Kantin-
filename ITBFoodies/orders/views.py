from django.http.response import JsonResponse
from django.shortcuts import render

from basket.basket import Basket

from .models import Order, OrderItem


def add(request):
    basket = Basket(request)

    user_id = request.user.id
    baskettotal = basket.get_total_price()

    order = Order.objects.create(user_id=user_id, full_name='name', total_paid=baskettotal, billing_status=True)
    order_id = order.pk

    for item in basket:
        OrderItem.objects.create(order_id=order_id, product=item['product'], price=item['price'], quantity=item['qty'])

    basket.clear()
    return render(request, 'payment/orderplaced.html')



def payment_confirmation(data):
    Order.objects.filter(order_key=data).update(billing_status=True)


def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders
