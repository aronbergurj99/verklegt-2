from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import PaymentProcessForm
from .models import Orders


def contact_phase(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PaymentProcessForm(request.POST)
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
        form = PaymentProcessForm(request.session)

    return render(request, 'orders/contact_phase.html', {'form': form})

def payment_phase(request):
    if request.method == 'POST':
        form = PaymentProcessForm(request.POST)
        if form.is_valid():
            request.session['credit_card_number'] = request.POST['credit_card_number']
            request.session['credit_card_holder'] = request.POST['credit_card_holder']
            request.session['credit_card_expiry_month'] = request.POST['credit_card_expiry_month']
            request.session['credit_card_expiry_year'] = request.POST['credit_card_expiry_year']
            request.session['pvc'] = request.POST['pvc']
            redirect('review_phase')
    else:
       form = PaymentProcessForm(request.session)

    return render(request, 'orders/payment_phase.html', {'form': form})

def review_phase(request):
    if request.method == 'POST':
        new_order = Orders.objects.create(
            status = 'HELLO GUYS',
            paid = True,
            total_price = 8.99,
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
            pvc = request.session['pvc'],
        )
        redirect('confirmation_phase')
        for key in list(request.session.keys()):
            if not key.startswith("_"):  # skip keys set by the django system
                del request.session[key]
    else:
        form = PaymentProcessForm(request.session)

    return render(request, 'orders/review_phase.html', context={
        'information': request.session
    })

def confirmation(request):

    return render(request, 'orders/confirmation.html')





# Create your views here.
def order_index(request):
    return render(request, 'orders/orders.html')


