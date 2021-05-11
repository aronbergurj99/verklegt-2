from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from account.forms import SignUpForm, ChangeInfoForm, LoginForm

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
    return render(request, 'account/account.html', context={'account': request.user, 'search_history': search_history, 'orders': orders})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'account/register.html', {
        'form': form
    })

def change_info(request):
    if request.method == 'POST':
        form = ChangeInfoForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            print(form)


    return render(request, 'account/change_info.html', {
        'form': ChangeInfoForm(instance=request.user)
    })

class UserLoginView(LoginView):

    LoginView.form_class = LoginForm
