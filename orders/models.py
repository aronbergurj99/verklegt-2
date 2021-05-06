from django.db import models
from django_countries.fields import CountryField


class Type(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.type)

class Orders(models.Model):
    status = models.CharField(max_length=80)
    date =  models.DateTimeField(auto_now_add=True)
    paid =  models.BooleanField()
    total_price =  models.DecimalField(decimal_places=2, max_digits=5)
    first_name =  models.CharField(max_length=80)
    last_name =  models.CharField(max_length=80)
    country =  models.CountryField(blank_label='(select country)')
    city =  models.CharField(max_length=80)
    address =  models.CharField(max_length=80)
    house_number = models.CharField(4)
    postal_code = models.CharField(max_length=10)


    def __str__(self):
        return '{}'.format(self.name)