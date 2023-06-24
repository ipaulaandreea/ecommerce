from django.urls import path
from ecommerce_app.views.api.product import views

urlpatterns = [
    path("products_data", views.productsData, name="productsData"),
]
