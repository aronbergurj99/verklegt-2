from django.contrib.auth.models import User
from django import forms
from django_countries.widgets import CountrySelectWidget

from orders.models import Orders
from django_countries.fields import CountryField


class PaymentProcessForm(forms.ModelForm):

    status = forms.CharField(required=False)
    paid = forms.BooleanField(required=False)
    total_price = forms.DecimalField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    country = CountryField()
    city = forms.CharField(required=False)
    street_name = forms.CharField(required=False)
    house_number = forms.CharField(required=False)
    postal_code = forms.CharField(required=False)
    credit_card_number = forms.CharField(required=False)
    credit_card_holder = forms.CharField(required=False)
    credit_card_expiry_month = forms.CharField(required=False)
    credit_card_expiry_year = forms.CharField(required=False)
    pvc = forms.CharField(required=False)

    class Meta:
        model = Orders
        fields = ('first_name', 'last_name', 'country', 'city', 'street_name', 'house_number','postal_code',
                  'credit_card_number', 'credit_card_holder', 'credit_card_expiry_month', 'credit_card_expiry_year', 'pvc')
        widgets = {'country': CountrySelectWidget()}

