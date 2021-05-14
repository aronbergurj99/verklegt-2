from django.db import models
from shop.models import Product
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Orders(models.Model):
    status = models.CharField(max_length=80)
    date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(blank=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=10)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    country = CountryField()
    city = models.CharField(max_length=80)
    street_name = models.CharField(max_length=80)
    house_number = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=10)
    credit_card_number = models.CharField(max_length=16)
    credit_card_holder = models.CharField(max_length=80)
    credit_card_expiry_month = models.CharField(max_length=2)
    credit_card_expiry_year = models.CharField(max_length=2)
    cvc = models.CharField(max_length=3)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return f'Date: {self.date.date()}, Price: {self.total_price}'
