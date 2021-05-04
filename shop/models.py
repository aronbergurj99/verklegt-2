from django.db import models
# Create your models here.


class Type(models.Model):
    type = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=255)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    stock = models.PositiveIntegerField()


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products', blank=True, null=True)


class Rating(models.Model):
    rating = models.DecimalField(decimal_places=2, max_digits=4)
    number_of_ratings = models.PositiveIntegerField()




