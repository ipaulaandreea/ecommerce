from django.urls import include, path

urlpatterns= [
    path("products/", include("ecommerce_app.urls.api.product.urls")),
    path("orders/", include("ecommerce_app.urls.api.order.urls")),
    # path("beforesubmit/", include("ecommerce_app.urls.api.order.urls"))
]