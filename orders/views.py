from django.shortcuts import render


# Create your views here.
def order_index(request):
    return render(request, 'orders/orders.html')