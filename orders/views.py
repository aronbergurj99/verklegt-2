from django.shortcuts import render
from shop.models import Cart

# Create your views here.
def index(request):
    return render(request, 'orders/orders.html', {
        "Create_order": Cart.objects.all()
        "Order_history": Cart.objects.all()
    })
