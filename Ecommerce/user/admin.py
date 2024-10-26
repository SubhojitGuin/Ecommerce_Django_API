from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):

    readonly_fields = ['email','password','created_at']

    list_display = ['id', 'first_name','last_name','email', 'phone', 'address', 'city', 'country', 'pin_code','created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'phone', 'address']
    list_per_page = 10

admin.site.register(User, UserAdmin)

class WishlistAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at']
    list_display = ['user','product','created_at','get_user_id','get_product_id']
    list_filter = ['created_at']
    search_fields = ['user', 'product']
    list_per_page = 10

    
    def get_user_id(self, obj):
        return obj.user.id
    get_user_id.short_description = 'user_id'  

    def get_product_id(self, obj):
        return obj.product.id
    get_product_id.short_description = 'product_id' 
    
admin.site.register(Wishlist, WishlistAdmin)