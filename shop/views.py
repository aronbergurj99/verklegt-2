from django.shortcuts import render
from .models import Product, Rating, ProductImage


# Create your views here.
def index(request):
    return render(request, 'shop/index.html', {
        "products": Product.objects.all().order_by('name'),
        "ratings": Rating.objects.all(),
        "images": ProductImage.objects.all().order_by('name')
    })
