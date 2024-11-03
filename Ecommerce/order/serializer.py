from rest_framework import serializers
from .models import *

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.CharField(source='product.price', read_only=True)
    product_image_path = serializers.CharField(source='product.image_path', read_only=True)
    class Meta:
        model = OrderItem
        fields = ['product_name', 'quantity', 'total_price', 'product', 'product_price', 'product_image_path']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = "__all__"