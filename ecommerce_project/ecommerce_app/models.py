from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField


class Category (models.Model):
    name=models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'categories'
        verbose_name_plural = "categories"

class Product (models.Model):
    title=models.CharField(max_length=150, null=False)
    description=models.TextField (blank=True)
    price=MoneyField(decimal_places=2, default=0, default_currency='USD',max_digits=11,null=False)
    image=models.ImageField(upload_to="uploads/product_photos", blank=True)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'products'
        verbose_name_plural = "products"
    
class Address(models.Model):
    name=models.CharField(max_length=50, null=False)
    city=models.CharField(max_length=50, null=False)
    street=models.CharField(max_length=150)
    number=models.IntegerField()
    flat=models.CharField(max_length=5, null=True, blank=True)
    apartment=models.IntegerField(null=True, blank=True)   

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'addresses'
        verbose_name_plural = "addresses"
    
class Client (models.Model):
    first_name=models.CharField(max_length=50, null=False)
    last_name=models.CharField(max_length=50, null=False)
    email=models.EmailField()
    address=models.ManyToManyField(Address)    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'clients'
        verbose_name_plural = "clients"

class Order (models.Model):
    client=models.ForeignKey(Client,on_delete=models.SET_NULL, null=True, blank=True)
    submitted=models.DateTimeField(auto_now_add=True)
    shipping_address=models.ForeignKey(Address, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'orders'
        verbose_name_plural = "orders"

class OrderItem (models.Model):
    product=models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity=models.IntegerField (default=0, null=False)
    order_id=models.ForeignKey(Order, on_delete=models.PROTECT, null=False)
    
    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'order_items'
        verbose_name_plural = "Order Items"
