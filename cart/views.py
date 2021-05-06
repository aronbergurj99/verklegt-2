from django.shortcuts import render
from shop.models import Product

# Create your views here.
def index(request):
    return render(request, 'cart/cart.html', {
        "products": Product.objects.all()
    })
