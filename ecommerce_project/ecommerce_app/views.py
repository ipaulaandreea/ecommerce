from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product, Address, Client, Order, OrderItem
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm


def login_user(request):
    if request.method=="POST": 
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("starting-page")
        else:
            messages.success (request, ("Something went wrong! Please try again."))
            return render(request, "ecommerce_app/login.html")

    else:
        return render(request, "ecommerce_app/login.html")
    
def register_user(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, ("Registration successful!"))
            return redirect ('starting-page')
    else: 
        form=UserForm()
    context={
    'form': form
    }
    return render(request, "ecommerce_app/register.html",context)

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been successfully logged out!"))
    return redirect('starting-page')

def starting_page(request):
    products=Product.objects.all()
    context={
        'products': products
    }
    return render (request, "ecommerce_app/starting_page.html", context)

class CartView(DetailView):
    model=Order
    template_name="ecommerce_app/cart.html"

def checkout(View):
    pass


    