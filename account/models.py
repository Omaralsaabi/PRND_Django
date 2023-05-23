from django.db import models
# Create your models here.

class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    phone = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    car = models.OneToOneField("core.Car", verbose_name=("car"), on_delete=models.CASCADE)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')

    

