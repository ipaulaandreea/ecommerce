from django.urls import path
from . import views

urlpatterns= [
path("", views.Store.as_view(), name="starting-page"),

]