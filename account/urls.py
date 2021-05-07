from django.contrib.auth.views import LoginView
from django.urls import path
from . import views


urlpatterns = [
    path('profile', views.profile, name="profile"),
    path('register', views.register, name="register"),
    path('login', LoginView.as_view(template_name='account/login.html'), name='login')
]
