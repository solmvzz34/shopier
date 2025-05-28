from django.urls import path
from . import views

urlpatterns = [
    path('odeme/', views.payment_view, name='shopier_payment'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('payment-cancel/', views.payment_cancel, name='payment_cancel'),
    path('shopier-callback/', views.shopier_callback, name='shopier_callback'),
]
