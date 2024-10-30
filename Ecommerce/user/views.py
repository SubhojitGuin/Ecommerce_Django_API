from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
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
      serializer = UserSerializer(user)
      return Response(serializer.data, status=status.HTTP_200_OK)
    else:
      return Response( {'error':'User not found'}, status=status.HTTP_400_BAD_REQUEST)
  except:
    return Response( {'error':'User not found'}, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['PUT'])
def update_user(request):
  try:
    data = request.data
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
  
@api_view(['POST'])
def add_to_wishlist(request):
  try:
    data = request.data
    serializer = WishlistSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'info':"Product added to wishlist successfully!!!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  except:
    return Response( {'error':'Incorrect Credentials'}, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['POST'])
def get_wishlist(request):
  try:
    data = request.data
    wishlist = Wishlist.objects.filter(user=data['user_id']).all()
    if wishlist:
      serializer = WishlistSerializer(wishlist, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
    else:
      return Response( {'error':'Wishlist is empty'}, status=status.HTTP_400_BAD_REQUEST)
  except:
    return Response( {'error':'Wishlist is empty'}, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['DELETE'])
def remove_from_wishlist(request):
  try:
    data = request.data
    # wishlist = Wishlist.objects.filter(user = data['user_id'], product = data['product_id']).first()
    wishlist = Wishlist.objects.get(user=data['user_id'], product=data['product_id'])
    if wishlist:
      wishlist.delete()
      return Response({'info':"Product removed from wishlist successfully!!!"}, status=status.HTTP_200_OK)
    else:
      return Response( {'error':'Product not found in wishlist'}, status=status.HTTP_400_BAD_REQUEST)
  except:
    return Response( {'error':'Product not found in wishlist'}, status=status.HTTP_400_BAD_REQUEST)