from django.urls import include, path

urlpatterns= [
    path("products/", include("ecommerce_app.urls.api.product.urls"))
]