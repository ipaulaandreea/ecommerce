from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Category, Product, Address, Client, Order, OrderItem

class StartingPageView(ListView):
    template_name="ecommerce_app/starting_page.html"
    model=Product

    def get_queryset(self):
        queryset=super().get_queryset()
        data=queryset[:3]
        return data
    #create pagination 
