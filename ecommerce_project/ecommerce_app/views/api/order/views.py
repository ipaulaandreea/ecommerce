from django.http import JsonResponse
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from ecommerce_app.models import Order, OrderLine, Product

@csrf_exempt
def orderData(request):
    if request.method=="POST":
        orderitems= json.loads(request.POST.get('orderitems'))

        data = orderitems.get('products')
        order=Order.objects.create()
        for item in data:
            product_id = item['product_id']
            qty = item['qty']
            product_instance = Product.objects.get(pk=product_id)
            order_line = OrderLine.objects.create(product_id=product_instance.id, qty=qty,price=qty*product_instance.price, order_id=order.id)
            order.total_cost+=order_line.price
            print(order.total_cost)
            order.save()
        data = {
            "orderId": order.id,
            "message": f"New item added to OrderLine with id: {order_line.id}",
            "message": f"New item added to Order with id: {order.id}"
        }
    
        return JsonResponse(data, status=201)

