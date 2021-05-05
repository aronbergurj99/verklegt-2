from django.shortcuts import render

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
def index(request):
    return render(request, 'account/account.html', context={'account': account, 'search_history': search_history, 'orders': orders})
