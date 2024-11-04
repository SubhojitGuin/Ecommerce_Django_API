from django.urls import path
from . import views

urlpatterns = [
    path('make_payment/<int:order_id>/', views.stripe_payment, name='make_payment')
]