from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    
class Food(models.Model):
    name=models.CharField(max_length=225)
    description=models.TextField()
    price=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
class Table(models.Model):
    number=models.CharField(max_length=2)
    capacity=models.CharField(max_length=2)
    is_available=models.BooleanField()
    (default=True)
    
class Order(models.Model):
    status_choice=[
        ('pending','Pending'),
        ('completed','Completed'),
        ('delivered','Delivered')
    ]
    payment_status=[
        ('p','PAID'),
        ('U','PENDING')
    ]
    user = models.ForeignKey(User,on_delete=models.Cascade)
    total_price=models.IntegerField()
    status=models.CharField(max_length=100,choices=status_choice)
    payment_status=models.CharField(max_length=1,choices=payment_status,default='P')
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.PROTECT)
    food=models.ForeignKey(Food,on_delete=models.PROTECT)
    