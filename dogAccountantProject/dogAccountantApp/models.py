# Create your models here.
from django.db import models
    # name, breed, color, and gender
class Dog(models.Model):
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=100)
    color = models.CharField(max_length=200)
    gender = models.CharField(max_length=300)
# created three dogs through the admin site.
# username, realName, accountNumber, balance
class Account(models.Model):
    username = models.CharField(max_length=500)
    realName = models.CharField(max_length=300)
    accountNumber = models.CharField(max_length=500)
    balance = models.IntegerField(default=0)
# Created three accounts through the admin site