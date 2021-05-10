from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from account.forms import SignUpForm
# from account.models import RegisteredUser

account = {
    'name': 'Jón Jónsson',
    'email': 'jon@gmail.com',
    'country': 'Iceland',
    'town': 'Akranes',
    'zip': '300',
    'Street': 'Melteigur 7'
}


search_history = [
    'Coco pops',
    'Cocoa puffs',
    'Lucky charms'
]

orders = [
    'Order #1',
    'Order #2',
    'Order #3',
    'Order #4',
    'Order #5'
]

# Create your views here.
def profile(request):
    return render(request, 'account/account.html', context={'account': account, 'search_history': search_history, 'orders': orders})

def register(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'account/register.html', {
        'form': SignUpForm()
    })

def login(request):
    return render(request, 'account/login.html', {
        'form': LoginForm()
    })