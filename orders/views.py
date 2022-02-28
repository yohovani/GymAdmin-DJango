from datetime import datetime
from django.shortcuts import redirect, render
from django.http import JsonResponse
from cart.models import CartItem
from store.models import Product
from .models import Order, OrderProduct, Payment
import random
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

import datetime

# Create your views here.
def place_order(request, total=0, quantity=0):
    current_user = request.user
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()

    if cart_count <= 0:
        return redirect('store')

    for cart_item in cart_items:
        total += cart_item.product.price * cart_item.quantity
        quantity += cart_item.quantity


    if request.method is not 'POST':
        order = Order.objects.filter(user=current_user, is_ordered=False).exists()
        if not order:
            data = Order()
            data.user = current_user
            data.order_note = "test"#request.POST['order_note']
            data.order_total = total
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            yr = int(datetime.date.today().strftime('%Y'))
            mt = int(datetime.date.today().strftime('%m'))
            dt = int(datetime.date.today().strftime('%d'))
            d = datetime.date(yr,mt,dt)
            current_date = d.strftime("%Y%m%d")
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()
        order = Order.objects.get(user=current_user, is_ordered=False)
        context = {
            'order':order,
            'cart_items':cart_items,
            'total':total,
        }
    return render(request, 'orders/place_order.html', context)
    
def payments(request):
    order = Order.objects.get(user=request.user, is_ordered = False)
    payment = Payment(
        user = request.user,
        payment_method = request.POST['metodo_pago'],
        payment_paid = request.POST['total_pago'],
        cambio = request.POST['cambio_cliente'],
    )
    payment.save()

    order.payment = payment
    order.is_ordered = True
    order.save()

    #Mover todos los carrito Items a la tabla Order Products
    cart_items = CartItem.objects.filter(user=request.user)
    order_products = []
    for item in cart_items:
        order_product = OrderProduct()
        order_product.order_id = order.id
        order_product.payment = payment
        order_product.user_id = request.user.id
        order_product.product_id = item.product_id
        order_product.quantity = item.quantity
        order_product.product_price = item.product.price
        order_product.save()
        order_products.append(order_product)

        product = Product.objects.get(id=item.product_id)
        product.stock -= item.quantity
        
        product.save()

    CartItem.objects.filter(user=request.user).delete()
        
    data = {
        'order':order,
        'payment': payment,
        'order_products':order_products,
    }
    return render(request,'orders/payment.html',data)

def order_complete(request):
    try:
        order = Order.objects.get(user=request.user, is_ordered=False)
        print(order)
        ordered_products = OrderProduct.objects.filter(order__id=order.id)
        subtotal = 0
        for i in ordered_products:
            subtotal += i.product_price*i.quantity
        
        payment = Payment.objects.get(pk=order.payment.pk)
        context = {
            'order': order,
            'ordered_products': ordered_products,
            'transID': payment.pk,
            'payment':payment,
            'subtotal':subtotal,
        }
    except(Payment.DoesNotExist, Order.DoesNotExist):
        return redirect('home')
    return render(request, 'orders/order_complete.html', context)