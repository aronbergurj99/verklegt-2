from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_index, name="order_index"),
]
