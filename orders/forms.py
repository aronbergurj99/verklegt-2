from django.contrib.auth.models import User
from django import forms


class PaymentPhase(forms.Form):
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    country = forms.CharField(max_length=80)
    city = forms.CharField(max_length=80)
    address = forms.CharField(max_length=80)
    house_number = forms.CharField(max_length=4)
    postal_code = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ('first_name', 'last_n ame', 'country', 'city', 'address', 'house_number','postal_code')