from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *
from django.contrib.auth.hashers import make_password, check_password

@api_view(['POST'])
def signup(request):
  try:
    data = request.data
    data['password'] = make_password(data['password'])
    serializer = UserSerializer(data=data)
    email = data['email']
    if serializer.is_valid():
        serializer.save()
        user = User.objects.filter(email = email).first()
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
    user = User.objects.filter(email = email).first()
    if user:
        if check_password(password, user.password):
            return Response({'user_id':user.id}, status=status.HTTP_200_OK)
        else:
            return Response({'error':'Invalid email-id or password'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'error':'Invalid email-id or password'}, status=status.HTTP_400_BAD_REQUEST)
  except:
    return Response( {'error':'Missing Credentials'}, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET'])
def get_user(request):
  try:
    data = request.data
    user = User.objects.filter(id = data.id).first()
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
    user = User.objects.filter(id = data.id).first()
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
    user = User.objects.filter(id = data.id).first()
    if user:
      user.delete()
      return Response({'info':"User deleted successfully!!!"}, status=status.HTTP_200_OK)
    else:
      return Response( {'error':'User not found'}, status=status.HTTP_400_BAD_REQUEST)
  except:
    return Response( {'error':'User not found'}, status=status.HTTP_400_BAD_REQUEST)