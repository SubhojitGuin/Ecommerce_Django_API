from django.contrib import admin
from .models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at']
    list_display = ['id', 'name','description','price','quantity','category','brand','created_at']
    list_filter = ['category','price','brand','quantity', 'created_at']
    search_fields = ['quantity', 'brand', 'category', 'price', 'name']
    list_per_page = 10

admin.site.register(Product, ProductAdmin)
