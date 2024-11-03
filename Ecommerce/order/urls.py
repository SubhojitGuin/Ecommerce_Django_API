from django.urls import path
from . import views

urlpatterns = [
    path('create_order/<int:user_id>/', views.create_order),
    path('get_order/<int:order_id>/', views.get_order),
    path('get_all_orders/<int:user_id>/', views.get_all_orders),
  ]
