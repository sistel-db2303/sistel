from django.db import models

# Create your models here.


class Customer(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    nik = models.CharField(max_length=16)

class Hotel(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    owner_first_name = models.CharField(max_length=50)
    owner_last_name = models.CharField(max_length=50)
    owner_phone_number = models.CharField(max_length=15)
    business_license = models.CharField(max_length=50)
    hotel_name = models.CharField(max_length=100)
    hotel_branch = models.CharField(max_length=100)
    street_name = models.CharField(max_length=100)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
