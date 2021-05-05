from django.shortcuts import render, get_object_or_404
from .models import Product, Rating, ProductImage
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(request):
    return render(request, 'shop/index.html', {
        "products": Product.objects.all().order_by('name'),
        "ratings": Rating.objects.all(),
        "images": ProductImage.objects.all().order_by('name')
    })


def get_product_by_id(request, id):
    return render(request, 'shop/detailed_product.html', {
        "product": get_object_or_404(Product, pk=id)
    })


def search(request):
    products = Product.objects.all().values('id','name', 'price')
    images = ProductImage.objects.all().values('image', 'product')
    return JsonResponse({'products': list(products),'images': list(images)}, safe=False)
