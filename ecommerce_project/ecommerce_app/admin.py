from django.contrib import admin
from .models import Category, Product, Address, Client, Cart

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Address)
admin.site.register(Client)
admin.site.register(Cart)