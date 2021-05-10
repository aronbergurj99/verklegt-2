from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from .views import UserLoginView


urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('register/', views.register, name="register"),


    path('login/', UserLoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout')
]
