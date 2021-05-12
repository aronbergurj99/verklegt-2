from django.http import JsonResponse
from django.shortcuts import render, redirect
from shop.models import Product
from django.views.decorators.http import require_POST
from .cart import Cart


# Create your views here.
def get_items_in_cart(request):
    cart = Cart(request)
    products = cart.get_items_in_cart()
    total_price = cart.get_total_price()

    return render(request, 'cart/cart.html', {
        "products": products,
        "total_price": total_price,
    })


def get_cart_length(request):
    # used for small cart icon on navbar, return the number of items in cart.
    cart = Cart(request)
    return JsonResponse({"cart-items": len(cart)})


@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add_to_cart(product_id)
    return redirect(cart.redirect_page())


@require_POST
def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove_from_cart(product_id)
    return redirect(cart.redirect_page())
