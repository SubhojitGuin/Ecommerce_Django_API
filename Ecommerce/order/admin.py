from django.contrib import admin
from .models import Product, Order, OrderItem

# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ['id', 'product', 'quantity', 'total_price']
    readonly_fields = ['total_price']
    extra = 0

    def total_price(self, obj):
        return obj.total_price
    total_price.short_description = "Total Price"

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_order_price' , 'order_status', 'payment_method' , 'payment_status', 'created_at'] 
    list_filter = ['order_status', 'payment_status', 'created_at']
    search_fields = ['order_status', 'payment_status']
    inlines = [OrderItemInline]

    def total_order_price(self, obj):
        return obj.total_price
    total_order_price.short_description = "Total Order Price"

admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
