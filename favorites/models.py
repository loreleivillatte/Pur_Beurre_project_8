from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    generic = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    grade = models.CharField(max_length=1)
    code = models.CharField(max_length=40)
    image = models.URLField()


class Favorite(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
