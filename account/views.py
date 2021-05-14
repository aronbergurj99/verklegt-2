from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from account.forms import SignUpForm, ChangeInfoForm, LoginForm, ChangeProfilePicture
from account.models import ProfilePicture
from orders.models import Orders

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
    if request.method == 'POST':
        form = ChangeProfilePicture(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get('file')
            try:
                profile_picture = ProfilePicture.objects.get(user=request.user)
                profile_picture.profile_image = image
                profile_picture.save()
            except:
                new_profile_picture = ProfilePicture(user=request.user, profile_image=image)
                new_profile_picture.save()

    try:
        profile_picture = ProfilePicture.objects.get(user=request.user).profile_image
    except:
        profile_picture = 'profile_pictures/basic_picture.jpg'
    return render(request, 'account/account.html', context={
        'account': request.user,
        'search_history': search_history,
        'orders': Orders.objects.filter(user=request.user),
        'profile_picture': profile_picture,
        'image_root': '/media/',
        'form': ChangeProfilePicture()
    })


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
    return render(request, 'account/change_info.html', {
        'form': ChangeInfoForm(instance=request.user)
    })

class UserLoginView(LoginView):
    LoginView.form_class = LoginForm