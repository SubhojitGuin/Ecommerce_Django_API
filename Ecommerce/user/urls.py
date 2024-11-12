from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # path('signup/verify/', views.verify_temporary_user, name='verify_temporary_user'),
    path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    path('profile/<int:user_id>/', views.get_user, name='get_user'),
    path('update/', views.update_user, name='edit_profile'),
    path('delete/', views.delete_user, name='delete_profile'),
    path('add_to_wishlist/<int:user_id>/<int:product_id>/',views.add_to_wishlist, name='add_to_wishlist'),
    path('get_wishlist/<int:user_id>/',views.get_wishlist, name='get_wishlist'),
    path('remove_from_wishlist/<int:user_id>/<int:product_id>/',views.remove_from_wishlist, name='remove_from_wishlist'),
    path('get_cart/<int:user_id>/',views.get_cart, name='get_cart'),
    path('add_to_cart/',views.add_to_cart, name='add_to_cart'),
    path('update_cart/<int:user_id>/',views.update_cart, name='update_cart'),
    path('clear_cart/<int:user_id>/',views.clear_cart, name='clear_cart'),
    path('remove_from_cart/<int:user_id>/<int:product_id>/',views.remove_from_cart, name='remove_from_cart')


    # path('profile/change_password/', views.change_password, name='change_password'),
    # path('profile/orders/', views.orders, name='orders'),
    # path('profile/order/<int:order_id>/', views.order, name='order'),
    # path('profile/order/<int:order_id>/cancel/', views.cancel_order, name='cancel_order'),
    # path('profile/order/<int:order_id>/return/', views.return_order, name='return_order'),
]