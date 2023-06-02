from django.urls import path
from . import views
from .views import CartView

urlpatterns= [
path("", views.starting_page, name="starting-page"),
path("login_user",views.login_user, name="login_user"),
path("register_user",views.register_user,name="register_user"),
# path("logout_user",views.logout_user,name="logout_user"),
path("cart/<int:pk>/", CartView.as_view(),name="cart"),
path("checkout/",views.checkout,name="checkout")

]