from typing import Optional
from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError('You must provide an email address')
        if not username:
            raise ValueError('You must provide a username')
        if not first_name:
            raise ValueError('You must provide a first name')
        if not last_name:
            raise ValueError('You must provide a last name')
        user=self.model(    
        email = self.normalize_email(email),
        first_name=first_name,
        last_name=last_name,
        username = username,
        )
        user.is_active=True

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, first_name, last_name, password):
        user=self.create_user(
            email = self.normalize_email(email),
            username = username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_admin=True
        user.is_staff=True
        user.is_active=True
        user.is_superuser=True
        user.save(using=self._db)
        return user
            

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=60, unique=True)
    username=models.CharField(max_length=30, unique=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    is_staff =models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name']
    
    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    # def __is_active__(self):
    #     return self.is_active
    class Meta:
        db_table = 'ecommerce_app_user'
    

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
    
class UserAddress(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=False, blank=False)
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
    

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=False, blank=False)
    address=models.ForeignKey(UserAddress, on_delete=models.CASCADE)
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
