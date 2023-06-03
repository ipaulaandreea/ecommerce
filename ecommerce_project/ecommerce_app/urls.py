from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns= [
path("", views.starting_page, name="starting-page"),
path("login_user",views.login_user, name="login_user"),
path("register_user",views.register_user,name="register_user"),
path("logout_user",views.logout_user,name="logout_user"),
path("cart", views.cart,name="cart"),
# path("checkout/",views.checkout,name="checkout"),
path("add_to_cart",views.add_to_cart, name="add_to_cart"),
path("login_user", auth_views.LoginView.as_view()),

]