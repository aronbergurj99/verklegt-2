from django.contrib.auth.models import User
from django.db import models
from shop.models import Product
# Create your models here.


class ProfilePicture(models.Model):
    profile_image = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)

