from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Type, Rating
from django.http import JsonResponse
from django.views.decorators.http import require_POST


# Create your views here.
def index(request):
    if 'type_filter' in request.GET:
        type_filter = request.GET['type_filter']
        if 'order' in request.GET:
            order = request.GET['order']
        else:
            order = 'name'

        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'image': x.productimage_set.first().image.url,
        } for x in Product.objects.filter(type__type__contains=type_filter).order_by(order)]
        return JsonResponse({"data": products})

    # Grabs all products from the db, and returns the main template, and products.
    return render(request, 'shop/index.html', {
        "products": Product.objects.all().order_by('name'),
        "types": Type.objects.all()
    })


def get_product_by_id(request, id):
    # Gets a single product from database from id, return 404 or the product.
    product = get_object_or_404(Product, pk=id)
    rating = 0
    number_of_ratings = 0
    if product.rating_set.first():
        rating = product.rating_set.first().get_total_rating(id)
        number_of_ratings = product.rating_set.first().get_number_of_rating(id)


    return render(request, 'shop/detailed_product.html', {
        "product": product,
        "rating": rating,
        "number_of_ratings": number_of_ratings
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



@require_POST
def rate_product(request, product_id):
    print(request.headers['Content-type'])
    next = request.POST.get('next', '/')
    if request.user.is_authenticated:
        if Product.objects.get(id=product_id).rating_set.all().filter(user=request.user).exists():
            if 'rating' in request.GET:
                rating = request.GET['rating']
                Product.objects.get(id=product_id).rating_set.all().filter(user=request.user).update(rating=rating)

            return redirect(next)
        else:
            if 'rating' in request.GET:
                rating = request.GET['rating']
                r = Rating(user=request.user, product=Product.objects.get(id=product_id), rating=rating)
                r.save()
            return redirect(next)
    else:
        return redirect('/accounts/login')
