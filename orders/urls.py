from django.urls import path
from . import views

urlpatterns = [
    path('contact-phase', views.get_contact_phase, name="contact_phase"),
]
