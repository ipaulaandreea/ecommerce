from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
from datetime import datetime


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
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to="uploads/product_photos", blank=True)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    

    def __str__(self):
        return self.title
    
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=""
        return url
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
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    first_name=models.CharField(max_length=50, null=False)
    last_name=models.CharField(max_length=50, null=False)
    email=models.EmailField()
    address=models.ManyToManyField(Address)    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'clients'
        verbose_name_plural = "clients"

class Order(models.Model):
    # orderline_id=models.ForeignKey(OrderLine, on_delete=models.CASCADE, null=False, blank=False)
    # user=models.ForeignKey(Client,on_delete=models.CASCADE, null=False, blank=False)
    created=models.DateTimeField(default=datetime.now())
    status=models.CharField(max_length=50, null=False)
    total_cost=models.IntegerField(default=0)

class OrderLine (models.Model):
    order=models.ForeignKey(Order, default=100, on_delete=models.CASCADE, null=False, blank=False)
    product=models.ForeignKey(Product,on_delete=models.CASCADE, null=False, blank=False)
    qty=models.IntegerField()
    price=models.IntegerField()
    created=models.DateTimeField(default=datetime.now())
    modified=models.DateTimeField(default=datetime.now())


class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def total_cost(self):
        total_cost=self.quantity*self.product.price
        return total_cost

    class Meta:
        db_table = 'carts'
        verbose_name_plural = "Carts"
