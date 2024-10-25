from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # path('signup/verify/', views.verify_temporary_user, name='verify_temporary_user'),
    path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    path('profile/<int:user_id>/', views.get_user, name='get_user'),
    path('update/<int:user_id>/', views.update_user, name='edit_profile'),
    path('delete/<int:user_id>/', views.delete_user, name='delete_profile'),
    # path('profile/change_password/', views.change_password, name='change_password'),
    # path('profile/orders/', views.orders, name='orders'),
    # path('profile/order/<int:order_id>/', views.order, name='order'),
    # path('profile/order/<int:order_id>/cancel/', views.cancel_order, name='cancel_order'),
    # path('profile/order/<int:order_id>/return/', views.return_order, name='return_order'),
]