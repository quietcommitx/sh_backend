from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
# User = get_user_model()
# Create your models here.
class Category(models.Model):    # Drink
   name = models.CharField(max_length=50)


class Food(models.Model):
   name = models.CharField(max_length=200)
   price = models.IntegerField()
   category = models.ForeignKey(Category, on_delete=models.CASCADE) 


class Table(models.Model):
   name = models.CharField(max_length=50)
   capacity = models.IntegerField(null=True)
   is_available = models.BooleanField(default=True)


class Order(models.Model):
   PENDING = "P"
   INPROGRESS = "IP"
   COMPLETED = "CO"
   DELIVERED = "D"
   CANCELLED = "CA"

   STATUS_CHOICES = {
      PENDING: "Pending",
      INPROGRESS: "In Progress",
      COMPLETED: "Completed",
      DELIVERED: "Delivered",
   }
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
   table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True, blank=True)
   status = models.CharField(max_length=2, choices=STATUS_CHOICES, default = PENDING)
   payment_status = models.BooleanField()


class OrderItem(models.Model):
   order = models.ForeignKey(Order, on_delete=models.PROTECT)
   food = models.ForeignKey(Food, on_delete=models.PROTECT)
