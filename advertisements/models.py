from django.db import models

# Create your models here.


class Ad(models.Model):
    user = models.ForeignKey("account.User", verbose_name=("user"), on_delete=models.CASCADE)
    car = models.ForeignKey("core.Car", verbose_name=("car"), on_delete=models.CASCADE)
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    likes = models.ManyToManyField("account.User", related_name='liked_ads')
    comments = models.ManyToManyField("account.User", through='Comment', related_name='commented_ads')



class Comment(models.Model):
    user = models.ForeignKey("account.User", on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    text = models.TextField()
