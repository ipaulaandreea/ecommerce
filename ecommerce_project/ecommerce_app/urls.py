from django.urls import path
from . import views

urlpatterns= [
path("", views.starting_page, name="starting-page"),
# path("product/<slug:slug>",views.SingleProductView.as_view(), name="product-detail-page"),
path("cart/", views.cart,name="cart"),
path("checkout/",views.checkout,name="checkout")

]