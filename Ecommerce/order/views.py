from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from user.models import *
from product.models import *
from .models import *
from .serializer import *

# Create your views here.
@api_view(['POST'])
def create_order(request, user_id):
  try:
    payment_method = request.data['payment_method']
    cart = get_object_or_404(Cart, user=user_id)
    address = request.data['address'] if "address" in request.data else cart.user.address 
    cart_dict = cart.cart

    for item, quantity in cart_dict.items():
      product = Product.objects.get(id=int(item))
      if product.quantity < quantity:
        return Response({'error':'Product out of stock'}, status=status.HTTP_400_BAD_REQUEST)

    order = Order.objects.create(user=cart.user, address=address, total_price=cart.total_price, payment_method=payment_method)
    order.save()

    for item, quantity in cart_dict.items():
      order_item = OrderItem.objects.create(order=order, product_id=int(item), quantity=quantity)
      order_item.save()

    return Response({"id" : order.id, "total_price": order.total_price}, status=status.HTTP_200_OK)
  except:
    return Response({'error':'Cart not found'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_order(request, order_id):
  try:
    order = Order.objects.get(id=order_id)
    order_serializer = OrderSerializer(order, many=False)
    return Response(order_serializer.data)
  except:
    return Response({'error':'Order not found'}, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET'])
def get_all_orders(request, user_id):
  try:
    orders = Order.objects.filter(user=user_id).all()
    order_serializer = OrderSerializer(orders, many=True)
    order_data = order_serializer.data
    return Response(order_data)
  except:
    return Response({'error':'Order not found'}, status=status.HTTP_400_BAD_REQUEST)
  
