from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email', 'phone', 'address', 'city', 'country', 'pin_code','created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'phone', 'address']
    list_per_page = 10

admin.site.register(User, UserAdmin)

class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user','product','created_at']
    list_filter = ['created_at']
    search_fields = ['user', 'product']
    list_per_page = 10
    
admin.site.register(Wishlist, WishlistAdmin)