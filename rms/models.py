from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
    
class Food(models.Model):
    name=models.CharField(max_length=225)
    description=models.TextField()
    price=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}-Rs.{self.price}"
    
class Table(models.Model):
    number=models.CharField(max_length=2)
    capacity=models.CharField(max_length=2)
    is_available=models.BooleanField(default=True)
    
class Order(models.Model):
    status_choice=[
        ('P','Pending'),
        ('C','Completed'),
        ('D','Delivered')
    ]
    payment_status=[
        ('p','PAID'),
        ('U','PENDING')
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    total_price=models.IntegerField()
    status=models.CharField(max_length=100,choices=status_choice,default='P')
    payment_status=models.CharField(max_length=1,choices=payment_status,default='P')
    
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.PROTECT)
    food=models.ForeignKey(Food,on_delete=models.PROTECT)
    