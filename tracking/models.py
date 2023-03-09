from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Farmer(models.Model):
    photo = models.ImageField(null=True,blank=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    contact = models.CharField(max_length=10)
    email= models.CharField(max_length=100)
    dateOfBirth= models.DateField()
    
    def __str__(self):
        return self.name        

class Cattle(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    date = models.DateField()
    owner = models.ForeignKey(Farmer, null=True, on_delete=models.CASCADE)
    pregnant = models.BooleanField(default=False)
    lost_status = models.BooleanField(default=False)
    def __str__(self):
        return self.name




# class GPSData(models.Model):
#     latitude = models.FloatField()
#     longitude = models.FloatField()
#     time = models.DateTimeField(auto_now_add=True)
