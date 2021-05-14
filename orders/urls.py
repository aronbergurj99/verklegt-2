from django.urls import path
from . import views

urlpatterns = [
    path('contact_phase', views.contact_phase, name="contact_phase"),
    path('payment_phase', views.payment_phase, name='payment_phase'),
    path('review_phase', views.review_phase, name='review_phase'),
    path('confirmation', views.confirmation, name='confirmation_phase')
]
