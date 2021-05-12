from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ProfilePicture(models.Model):
    profile_image = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Country(models.Model):
    country = models.CharField(max_length=80)

class Address(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.CharField(max_length=80)
    street_name = models.CharField(max_length=80)
    house_number = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=80)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

