from typing import Any
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from ..models import Product, Cart, User
from ..forms import UserCreationForm
from django.http import JsonResponse

def login_user(request):
    if request.method=="POST": 
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("starting-page")
        else:
            messages.success (request, ("Something went wrong! Please try again."))
            return render(request, "ecommerce_app/login.html")
    else:
        return render(request, "ecommerce_app/login.html")
    
def register_user(request):
    try:
        if request.method=="POST":
            form=UserCreationForm(request.POST)
            if form.is_valid():
                # first_name=form.cleaned_data['first_name']
                # last_name=form.cleaned_data['last_name']
                # username=form.cleaned_data['username']
                # email=form.cleaned_data['email']
                # password1=form.cleaned_data['password1']
                # password2=form.cleaned_data['password2']
                form.save()
                 
                # user=form.cleaned_data['user']
                # authenticate(first_name=first_name, last_name=last_name, username=username,email=email)
                # login_user()
                messages.success(request, ("Registration successful!"))
                return redirect ('starting-page')
        else: 
            form=UserCreationForm()
        # context={
        # 'form': form
        # }
    except Exception as e:
        messages.error(request, ("Something went wrong"))
    
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



def checkout(request):
    return render (request, "ecommerce_app/checkout.html")

@login_required(redirect_field_name="login_user")
def ordersubmitted (request):
    return render (request, "ecommerce_app/ordersubmitted.html")


def access_session(request):
    if request.method=="GET":
        session_id = request.session.session_key
    return JsonResponse({'session_id': session_id})

def beforesubmit(request):
    return render (request, "ecommerce_app/beforesubmit.html")