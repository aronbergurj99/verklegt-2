from django.db import models
from shop.models import Product


class Orders(models.Model):
    status = models.CharField(max_length=80)
    date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(blank=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=5)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    country = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    street_name = models.CharField(max_length=80)
    house_number = models.CharField(max_length=4)
    postal_code = models.CharField(max_length=10)
    credit_card_number = models.CharField(max_length=16)
    credit_card_holder = models.CharField(max_length=80)
    credit_card_expiry_month = models.CharField(max_length=2)
    credit_card_expiry_year = models.CharField(max_length=2)
    pvc = models.CharField(max_length=3)


    def __str__(self):
        return '{}'.format(self.date)


class Ordered_product(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.order)