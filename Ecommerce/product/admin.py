from django.contrib import admin
from .models import *

# Register your models here.

class ReviewInlineAdmin(admin.TabularInline):
    model = Review
    readonly_fields = ['rating', 'created_at', 'updated_at']
    fields = ['user','product','rating','review','verified_purchase']
    extra = 0
    
    def has_delete_permission(self, request, obj=None):
        return False
    
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at']
    list_display = ['id', 'name','description','price','quantity','category','brand','created_at']
    list_filter = ['category','price','brand','quantity', 'created_at']
    search_fields = ['quantity', 'brand', 'category', 'price', 'name']
    list_per_page = 10
    inlines = [ReviewInlineAdmin]

admin.site.register(Product, ProductAdmin)

class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at','updated_at']
    list_display = ['user','product','review','rating','verified_purchase']
    list_filter = ['rating','verified_purchase','created_at']
    search_fields = ['rating','verified_purchase','created_at']
    list_per_page = 10

admin.site.register(Review, ReviewAdmin)
