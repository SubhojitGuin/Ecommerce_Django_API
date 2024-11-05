from django.urls import path
from . import views

urlpatterns = [
    path('list/<int:user_id>/', views.product_list, name='product_list'),
    path('detail/<int:product_id>/', views.product_detail, name='product_detail'), 
    path('create/', views.product_create, name='product_create'),
    path('update/', views.product_update, name='product_update'),
    path('delete/', views.product_delete, name='product_delete'),
    path('search/', views.product_search, name='product_search'),
    path('filterby_category/', views.product_category, name='product_category'),
    path('filterby_brand/', views.product_brand, name='product_brand'),
    path('filterby_price/', views.product_price, name='product_price'),
    path('add_review/', views.add_review, name='add_review'),
    path('get_review/<int:product_id>/', views.get_reviews, name='get_review'),
    path('update_review/<int:user_id>/<int:product_id>/', views.update_review, name='update_review'),
    path('delete_review/<int:user_id>/<int:product_id>/', views.delete_review, name='delete_review'),
]