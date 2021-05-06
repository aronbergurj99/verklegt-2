from django.shortcuts import render, redirect
from shop.models import Product
from django.views.decorators.http import require_POST


# Create your views here.
def get_items_in_cart(request):
    products = []
    total_price = 0.0
    if request.session.get('cart', False):
        for product_id, value in request.session['cart'].items():
            print(value)
            __product = Product.objects.get(pk=product_id)
            products.append((__product, value['quantity']))
            total_price += float(__product.price) * int(value['quantity'])

    return render(request, 'cart/cart.html', {
        "products": products,
        "total_price": total_price,
    })


# Here are the post request for adding, and removing items from cart.
# TODO create some helper class to deal with cart behavior.

@require_POST
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    product_info = {
        "price": str(product.price),
        "quantity": 1,
    }

    if request.session.get('cart', False):
        if request.session['cart'].get(str(product.id), False):
            request.session['cart'][str(product.id)]['quantity'] += 1
        else:
            request.session['cart'][str(product.id)] = product_info
    else:
        request.session['cart'] = {}
        request.session['cart'][str(product.id)] = product_info
    request.session.modified = True

    current_page = request.POST.get('next', '/')
    return redirect(current_page)


@require_POST
def remove_from_cart(request, product_id):

    request.session['cart'][str(product_id)]['quantity'] -= 1
    if request.session['cart'][str(product_id)]['quantity'] <= 0:
        del request.session['cart'][str(product_id)]

    request.session.modified = True
    current_page = request.POST.get('next', '/')
    return redirect(current_page)
