from django.db import models
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
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.DecimalField(decimal_places=2, max_digits=4)
    number_of_ratings = models.PositiveIntegerField()

    def __str__(self):
        return '{}'.format(self.product.name)


