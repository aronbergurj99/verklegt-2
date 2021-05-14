from django.contrib.auth.models import User
from django import forms
from django_countries.widgets import CountrySelectWidget
from orders.models import Orders


class PaymentProcessForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('first_name', 'last_name', 'country', 'city', 'street_name', 'house_number','postal_code',
                  'credit_card_number', 'credit_card_holder', 'credit_card_expiry_month', 'credit_card_expiry_year', 'pvc')

class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('first_name', 'last_name', 'country', 'city', 'street_name', 'house_number', 'postal_code')
        widgets = {'country': CountrySelectWidget()}

class PaymentInfoForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('credit_card_number', 'credit_card_holder', 'credit_card_expiry_month', 'credit_card_expiry_year', 'pvc')

