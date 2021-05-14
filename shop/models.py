from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Type(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.type)


class Product(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=255)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()

    def __str__(self):
        return '{}'.format(self.name)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products', blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.product.name)

    def get_total_rating(self, product_id):
        product = Product.objects.get(id=product_id)
        rating = sum([item.rating for item in product.rating_set.all()]) / self.get_number_of_rating(product_id)
        return rating


    def get_number_of_rating(self, product_id):
        product = Product.objects.get(id=product_id)
        ratings = product.rating_set.all()
        return len(ratings)
