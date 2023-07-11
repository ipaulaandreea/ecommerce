from django.http import JsonResponse
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from ecommerce_app.models import Order, OrderLine, Product
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User



@login_required(redirect_field_name="login_user")
def orderData(request):
    if request.method=="POST":
        orderitems= json.loads(request.POST.get('orderitems'))
        session_id= json.loads(request.POST.get('sessionID'))
        data = orderitems.get('products')
        try:

            session = Session.objects.get(session_key=session_id)
            user_id = session.get_decoded().get('_auth_user_id')
            user = User.objects.get(pk=user_id)
        except Session.DoesNotExist:
            pass

        userdata_id=request.user.id
        order=Order.objects.create(user_id=userdata_id)
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

