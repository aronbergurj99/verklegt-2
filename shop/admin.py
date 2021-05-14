from django.contrib import admin

# Register your models here.
from .models import Type, Product, ProductImage, Rating

admin.site.register(Type)
admin.site.register(Product)
admin.site.register(ProductImage)

