from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_items_in_cart, name="cart"),
    path('add-to-cart/<int:product_id>', views.add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<int:product_id>', views.remove_from_cart, name="remove-from-cart"),
    path('get-cart-len', views.get_cart_length, name='cart-length'),
]
