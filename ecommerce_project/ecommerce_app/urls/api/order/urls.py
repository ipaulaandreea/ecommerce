from django.urls import path
from ecommerce_app.views.api.order import views


urlpatterns= [
    path("create", views.orderData, name="orderData"),
]