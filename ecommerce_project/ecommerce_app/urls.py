from django.urls import path
from . import views

urlpatterns= [
path("", views.StartingPageView.as_view(), name="starting-page"),
path("product/<slug:slug>",views.SingleProductView.as_view(), name="product-detail-page"),

]