from django.urls import include, path
from ..views import views
from django.contrib.auth import views as auth_views

urlpatterns= [
path("", views.starting_page, name="starting-page"),
path("login_user",views.login_user, name="login_user"),
path("register_user",views.register_user,name="register_user"),
path("logout_user",views.logout_user,name="logout_user"),
path("cart", views.cart,name="cart"),
path("cart/ordersubmitted", views.ordersubmitted,name="ordersubmitted"),
path("checkout/",views.checkout,name="checkout"),
# path("add_to_cart",views.add_to_cart, name="add_to_cart"),
# path("remove_from_cart",views.add_to_cart, name="remove_from_cart"),
path("login_user", auth_views.LoginView.as_view()),
path("api/", include("ecommerce_app.urls.api.urls")),
path("access_session/",views.access_session,name="access_session")

]