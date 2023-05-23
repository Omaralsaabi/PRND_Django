from django.db import models
from core import *
# Create your models here.

class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    phone = models.IntegerField(max_length=50)
    image = models.ImageField(upload_to='images/')
    car = models.OneToOneField("core.Car", verbose_name=("car"), on_delete=models.CASCADE)
    

