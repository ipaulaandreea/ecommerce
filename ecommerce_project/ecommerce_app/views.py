from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View

from .models import Category, Product, Address, Client, Order, OrderItem

class StartingPageView(ListView):
    template_name="ecommerce_app/starting_page.html"
    model=Product
    context_object_name="products"

    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset
    #create pagination 

class SingleProductView(View):
 
    def get(self,request,slug):
        product=Product.objects.get(slug=slug)
        description=Product.objects.get(description=description)
        price=Product.objects.get(price=price)
        
        context={
            "product": product,
            "description":description,
            "price":price,
        }
        return render(request, "ecommerce_app/product-detail.html", context)
