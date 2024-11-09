from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from product.models import *
from product.serializer import *
from .serializer import *
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
@api_view(['POST'])
def signup(request):
  try:
    data = request.data
    data['password'] = make_password(data['password'])
    serializer = UserSerializer(data=data)
    email = data['email']
    if serializer.is_valid():
        serializer.save()
        user = User.objects.filter(email=email).first()
        if user:
            user_id = user.id
        return Response({'user_id':user_id}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  except:
    return Response( {'error':'Missing Credentials'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
  try:
    data = request.data
    email = data['email']
    password = data['password']
    user = User.objects.filter(email=email).first()
    if user:
        if check_password(password, user.password):
            return Response({'user_id':user.id}, status=status.HTTP_200_OK)
        else:
            return Response({'error':'Invalid email-id or password'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'error':'Invalid email-id or password'}, status=status.HTTP_400_BAD_REQUEST)
  except:
    return Response( {'error':'Missing Credentials'}, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET'])
def get_user(request, user_id):
  try:
    user = User.objects.filter(id=user_id).first()
    if user:
      serializer = UserModifiedSerializer(user)
      return Response(serializer.data, status=status.HTTP_200_OK)
    else:
      return Response( {'error':'User not found'}, status=status.HTTP_400_BAD_REQUEST)
  except:
    return Response( {'error':'User not found'}, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['PUT'])
def update_user(request):
  try:
    data = request.data
    data = {k: v for k, v in data.items() if v}
    user = User.objects.get(id=data['id'])
    if 'password' in data:
        data['password'] = make_password(data['password'])
    if user:       
        serializer = UserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'info':"Profile updated successfully!!!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response( {'error':'User not found'}, status=status.HTTP_400_BAD_REQUEST)
  except:
    return Response( {'error':'User not found'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request):
  try:
    data = request.data
    user = User.objects.get(id=data['id'])
    if user:
      user.delete()
      return Response({'info':"User deleted successfully!!!"}, status=status.HTTP_200_OK)
    else:
      return Response( {'error':'User not found'}, status=status.HTTP_400_BAD_REQUEST)
  except:
    return Response( {'error':'User not found'}, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET'])
def add_to_wishlist(request,user_id ,product_id):
  try:
    data = {
      'user': user_id,
      'product': product_id
    }
    serializer = WishlistSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'info':"Product added to wishlist successfully!!!"}, status=status.HTTP_201_CREATED)
    return Response({'error':'Incorrect Credentials'}, status=status.HTTP_400_BAD_REQUEST)
  except:
    return Response( {'error':'Incorrect Credentials'}, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET'])
def get_wishlist(request , user_id):
  try:
    wishlist = Wishlist.objects.filter(user=user_id).all()
    if wishlist:
      serializer = WishlistSerializer(wishlist, many=True)
      wishdict = serializer.data
      for wish in wishdict:
        product = Product.objects.filter(id=wish['product']).first()
        wish['product']  = ProductSerializer(product).data
        # i['product'] = product.name
        # i['description'] = product.description
        # i['price'] = product.price
        # i['brand'] = product.brand 
        if product.quantity > 0:
          wish['product']['available'] = 'In stock'
        else:
          wish['product']['available'] = 'Out of stock'
      return Response(wishdict, status=status.HTTP_200_OK)
    else:
      return Response( {'error':'Wishlist is empty'}, status=status.HTTP_200_OK)
  except:
    return Response( {'error':'Wishlist is empty'}, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['DELETE'])
def remove_from_wishlist(request,user_id, product_id):
  try:  
    # wishlist = Wishlist.objects.filter(user = data['user_id'], product = data['product_id']).first()
    wishlist = Wishlist.objects.get(user=user_id, product=product_id)
    if wishlist:
      wishlist.delete()
      return Response({'info':"Product removed from wishlist successfully!!!"}, status=status.HTTP_200_OK)
    else:
      return Response( {'error':'Product not found in wishlist'}, status=status.HTTP_400_BAD_REQUEST)
  except:
    return Response( {'error':'Product not found in wishlist'}, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['POST'])
def add_to_cart(request):
  try:
    data = request.data
    user_id = data['user_id']
    product_id = data['product_id']
    # total_price = 0
    cart_obj = Cart.objects.filter(user=user_id).first()
    if not cart_obj:
      cart = {}
    else:
      cart = cart_obj.cart
    cart[product_id] = 1
    # for product, quantity in cart.items():
    #   product_obj = Product.objects.get(id=product)
    #   total_price += product_obj.price * quantity
    dict = {
      "user": user_id,
      "cart": cart
      # "total_price": total_price
    }
    serializer = CartSerializer(cart_obj, data=dict, partial = True)
    if serializer.is_valid():
      serializer.save()
      return Response({"info": "Added to cart"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  except:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_cart(request, user_id):
  try:
    cart_obj = Cart.objects.get(user=user_id)
    if cart_obj:
      cart = cart_obj.cart
      cart_dict = {}
      cart_dict["viewCart"] = True
      for key, value in cart.items():
        product = Product.objects.filter(id=key).first()
        cart_dict[key] = ProductSerializer(product).data
        cart_dict[key]['cart_quantity'] = value
      return Response({"cart" : cart_dict , "total_price" : cart_obj.total_price}, status=status.HTTP_200_OK)
    else:
      return Response({'viewCart': False}, status=status.HTTP_400_BAD_REQUEST)
  except:
    return Response({'error': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def remove_from_cart(request, user_id, product_id):
  try:
    cart_obj = Cart.objects.get(user=user_id)
    if cart_obj:
      cart = cart_obj.cart
      if product_id in cart:
        del cart[product_id]
        cart_obj.cart = cart
        cart_obj.save()
        return Response({'info': 'Product deleted from cart'}, status=status.HTTP_200_OK)
      else:
        return Response({'error': 'Product not found in cart'}, status=status.HTTP_400_BAD_REQUEST)
    else:
      return Response({'error': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)
  except:
    return Response({'error': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['DELETE'])
def clear_cart(request, user_id):
  try:
    cart_obj = Cart.objects.get(user=user_id)
    if cart_obj:
      cart_obj.delete()
      return Response({'info': 'Cart cleared successfully'}, status=status.HTTP_200_OK)
    else:
      return Response({'error': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)
  except:
    return Response({'error': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['POST'])
def update_cart(request, user_id):
  try:
    data = request.data
    cart_dict = data['cart']
    cart_obj = Cart.objects.get(user=user_id)
    total_price = 0
    if cart_obj:
      cart_dict = {k: v for k, v in cart_dict.items() if v}    
      # for product, quantity in cart_dict.items():
      #   product_obj = Product.objects.get(id=product)
      #   total_price += product_obj.price * quantity
      data = {
        'user': user_id,
        'cart': cart_dict
        # 'total_price': total_price
      }
      serializer = CartSerializer(cart_obj, data=data, partial=True)
      if serializer.is_valid():
        serializer.save()
        cart_obj = Cart.objects.get(user=user_id)
        return Response({'info': 'Cart updated successfully', 'total_price': cart_obj.total_price}, status=status.HTTP_200_OK)
    else:
      return Response({'error': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)
  except:
    return Response({'error': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)

  