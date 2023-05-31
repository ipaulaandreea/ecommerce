from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View

from .models import Category, Product, Address, Client, Order, OrderItem

def starting_page(request):
    products=Product.objects.all()
    context={
        'products': products
    }
    
    return render (request, "ecommerce_app/starting_page.html", context)
    # template_name="ecommerce_app/starting_page.html"
    # model=Product
    # context_object_name="products"

    # def get_queryset(self):
    #     queryset=super().get_queryset()
    #     return queryset
    # #create pagination 

def cart(request):
    context={}
    return render (request, "ecommerce_app/cart.html", context)

def checkout(View):
    pass

def auth(request):
    context={}
    return render (request, "ecommerce_app/auth.html", context)
