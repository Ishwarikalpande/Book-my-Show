import total
from django.db import models


# Create your models here.
class Theatre(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    seating = models.IntegerField()
    screen = models.IntegerField()


class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=40)
    movie = models.CharField(max_length=23)
    theatre = models.CharField(max_length=34)
    time = models.TimeField()
    date = models.DateField()

class User1(models.Model):
    name= models.CharField(max_length=70)
    email = models.EmailField(max_length=40)
    message = models.CharField(max_length=200)
    contact = models.IntegerField()


class User2(models.Model):
    name= models.CharField(max_length=70)
    email= models.EmailField(max_length=40)
    user_name= models.CharField(max_length=70)
    password =models.CharField(max_length=90)
