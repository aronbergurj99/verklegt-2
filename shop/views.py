from django.shortcuts import render, get_object_or_404
from .models import Product, Type
from django.http import JsonResponse


# Create your views here.
def index(request):
    if 'type_filter' in request.GET:
        type_filter = request.GET['type_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            #'image': x.productimage_set.first.image,
        } for x in Product.objects.filter(type__type__contains=type_filter)]
        print(products)
        return JsonResponse({"data": products})

    # Grabs all products from the db, and returns the main template, and products.
    return render(request, 'shop/index.html', {
        "products": Product.objects.all().order_by('name'),
        "types": Type.objects.all()
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
