from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import PaymentProcessForm, PaymentInfoForm, ContactInfoForm
from .models import Orders
from cart.cart import Cart


def contact_phase(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactInfoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            request.session['first_name'] = request.POST['first_name']
            request.session['last_name'] = request.POST['last_name']
            request.session['country'] = request.POST['country']
            request.session['city'] = request.POST['city']
            request.session['street_name'] = request.POST['street_name']
            request.session['house_number'] = request.POST['house_number']
            request.session['postal_code'] = request.POST['postal_code']
            return redirect('payment_phase')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactInfoForm(request.session)
    cart = Cart(request)
    products = cart.get_items_in_cart()

    return render(request, 'orders/contact_phase.html', {'form': form, 'cart': products})

def payment_phase(request):
    if request.method == 'POST':
        form = PaymentInfoForm(request.POST)
        print(form.errors)
        if form.is_valid():
            request.session['credit_card_number'] = request.POST['credit_card_number']
            request.session['credit_card_holder'] = request.POST['credit_card_holder']
            request.session['credit_card_expiry_month'] = request.POST['credit_card_expiry_month']
            request.session['credit_card_expiry_year'] = request.POST['credit_card_expiry_year']
            request.session['pvc'] = request.POST['pvc']
            return redirect('review_phase')
    else:
        form = PaymentInfoForm(request.session)
    cart = Cart(request)
    products = cart.get_items_in_cart()

    return render(request, 'orders/payment_phase.html', {'form': form, 'cart': products})

def review_phase(request):
    if request.method == 'POST':
        form = PaymentProcessForm(request.session)
        if form.is_valid():
            new_order = Orders.objects.create(
                status = 'Sauce',
                paid = True,
                total_price = get_full_price(request.session['cart']),
                first_name = request.session['first_name'],
                last_name=request.session['last_name'],
                country = request.session['country'],
                city = request.session['city'],
                street_name = request.session['street_name'],
                house_number = request.session['house_number'],
                postal_code = request.session['postal_code'],
                credit_card_number = request.session['credit_card_number'],
                credit_card_holder = request.session['credit_card_holder'],
                credit_card_expiry_month = request.session['credit_card_expiry_month'],
                credit_card_expiry_year = request.session['credit_card_expiry_year'],
                pvc = request.session['pvc']
            )
            if request.user.is_authenticated:
                new_order.user = request.user
                new_order.save()
            for key in list(request.session.keys()):
                if not key.startswith("_") and not key == 'search-history':  # skip keys set by the django system
                    del request.session[key]
            return redirect('confirmation_phase')
    cart = Cart(request)
    products = cart.get_items_in_cart()

    return render(request, 'orders/review_phase.html', {'information': get_information(request.session), 'cart': products})

def confirmation(request):

    return render(request, 'orders/confirmation.html')

def get_full_price(cart):
    total_price = 0
    for key, value in cart.items():
        total_price += value['price']
    return round(total_price, 2)

def get_information(session):
    ret_dict = {}
    for key, value in session.items():
        if not key.startswith("_") and not key == 'search-history' and not key == 'cart':
            new_key = key.replace('_', ' ').capitalize()
            ret_dict[new_key] = value
    return ret_dict
