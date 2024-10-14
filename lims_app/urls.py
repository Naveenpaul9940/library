from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', home, name='home'),
    path('readers/', readers, name='readers'),
    path('shopping/', shopping, name='shopping'),
    path('save/', save_student, name='save_student'),
    path('collections/', collections, name='collections'),
    path('add-to-cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('checkout/', checkout, name='checkout'),
    path('payment-info/', payment_info, name='payment_info'),  # New payment info URL
    path('payment-success/', payment_success, name='payment_success'),
]
