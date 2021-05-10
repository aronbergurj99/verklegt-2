from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    def __init__(self):
        # simple trick to put class on each field!
        super(SignUpForm, self).__init__()
        for field_name, field in self.fields.items():
            clean_name = ''.join(char for char in field_name if char.isalpha() or char == '_').replace('_', ' ')
            print(clean_name)
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['id'] = field_name
            field.widget.attrs['aria-describedby'] = field_name + '-help'
            field.widget.attrs['placeholder'] = 'Enter ' + clean_name

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


