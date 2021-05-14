from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('products/<int:id>', views.get_product_by_id, name='product-details'),
    path('search', views.search, name="search"),
    path('products/rate/<int:product_id>', views.rate_product, name='rate-product')
]
