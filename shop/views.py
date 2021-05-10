from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import JsonResponse


# Create your views here.
def index(request):
    # Grabs all products from the db, and returns the main template, and products.
    return render(request, 'shop/index.html', {
        "products": Product.objects.all().order_by('name')
    })


def get_product_by_id(request, id):
    # Gets a single product from database from id, return 404 or the product.
    return render(request, 'shop/detailed_product.html', {
        "product": get_object_or_404(Product, pk=id)
    })


def search(request):
    # Gets all the products from the database, returns them as json for live search.
    products = [{
        'id': x.id,
        'name': x.name,
        'price': x.price,
        'image': x.productimage_set.first().image.url,
    } for x in Product.objects.all()]

    return JsonResponse({'data': products}, safe=False)
