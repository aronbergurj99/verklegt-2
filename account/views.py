from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from account.forms import SignUpForm, ChangeInfoForm, LoginForm, ChangeProfilePicture
from account.models import ProfilePicture, SearchHistory
from shop.models import Product
from django.views.decorators.http import require_POST

account = {
    'name': 'Jón Jónsson',
    'email': 'jon@gmail.com',
    'country': 'Iceland',
    'town': 'Akranes',
    'zip': '300',
    'Street': 'Melteigur 7'
}

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

    search_history = request.user.searchhistory_set.all().order_by('-datetime')[:10]
    search_history = [get_object_or_404(Product, id=item.product_id) for item in search_history]

    return render(request, 'account/account.html', context={
        'account': request.user,
        'search_history': search_history,
        'orders': orders,
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


def get_search_history(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        data = list(user.searchhistory_set.all().order_by('datetime').values())
        data = user.searchhistory_set.all().order_by('-datetime').values('product_id')
        products = []
        for item in data:
            products.append(get_object_or_404(Product, id=item['product_id']))
        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'image': x.productimage_set.first().image.url,
        } for x in products]
    else:
        pass
    return JsonResponse({"data": products}, safe=False)


@require_POST
def add_search_history(request, product_id):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        product = get_object_or_404(Product, id=product_id)
        sh = SearchHistory(user=user, product=product)
        sh.save()
        print('success')
    else:
        print('fail')
        pass
    return JsonResponse({"message": "successfully added search to search history"})
