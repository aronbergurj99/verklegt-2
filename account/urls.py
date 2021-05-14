from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from .views import UserLoginView


urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('register/', views.register, name="register"),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('change_info/', views.change_info, name="change_info"),
    # for live search
    path('search-history', views.get_search_history, name="search-history"),
    path('search-history/<int:product_id>', views.add_search_history, name="search-history-add")
]
