from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=70)
    movie_name = models.CharField(max_length=50)
    theater = models.CharField(max_length=40)
    date = models.DateField()
    time = models.TimeField()
