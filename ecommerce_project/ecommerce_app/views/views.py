from typing import Any
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from ..models import Product, Cart
from ..forms import UserForm

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


@login_required(redirect_field_name="login_user")
def cart(request):
    user=request.user
    cartitems=Cart.objects.filter(user=user)
    cart_amt=0
    for cartitem in cartitems:
        prod_amt= (cartitem.product.price)*(cartitem.quantity)
        cart_amt += prod_amt
    context={
    'cartitems': cartitems,
    'cart_amt':cart_amt
    }
    return render (request, "ecommerce_app/cart.html", context)


def add_to_cart(request):
    if request.method=='POST':
        user=request.user
        product_id=request.POST.get('product_id')
        product=Product.objects.get(id=product_id)
        Cart(user=user, product=product).save()
        messages.success(request, ("Item successfully added to cart!"))
        return redirect('starting-page')

# def remove_from_cart(request):
#      if request.method=='POST':
#         user=request.user
#         product_id=request.POST.get('cartitem_product')
#         product=Product.objects.get(id=product_id)
#         Cart(user=user, product=product).delete()
#         messages.success(request, ("Item successfully removed cart!"))
#         return redirect('cart')

def modify_product_quantity():
    pass

def checkout(request):
    return render (request, "ecommerce_app/checkout.html")

    