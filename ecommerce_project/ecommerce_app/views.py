from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Category, Product, Address, Client, Order, OrderItem

class Store(ListView):
    pass
