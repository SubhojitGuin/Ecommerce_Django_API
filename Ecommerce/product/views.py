from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def product_detail(request):
  try:
    data = request.data
    print(data)
    product = Product.objects.get(id=data['id'])
    print(product)
    if product:
        quantity = product.quantity
        if quantity == 0:
           available = "Out of stock"
        else:
           available = "In stock"
        serializer = ProductSerializer(product, many=False)
        data = serializer.data
        data['available'] = available
        return Response(data)
    else:
        return Response({'error':'Product not found'}, status=status.HTTP_400_BAD_REQUEST)
  except:
    return Response({'error':'Product not found'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def product_create(request):
  try:
    data = request.data
    serializer = ProductSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    return Response({"id" : serializer.data['id']}, status=status.HTTP_200_OK)
  except:
    return Response( {'error':'Missing Required Data'}, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['PUT'])
def product_update(request):
  try:
    data = request.data
    product = Product.objects.get(id=data['id'])
    if product:
        serializer = ProductSerializer(product, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response({'message':'Product Updated'}, status=status.HTTP_200_OK)
    else:
      return Response( {'error':'Product not found'}, status=status.HTTP_400_BAD_REQUEST)
  except:
    return Response( {'error':'Missing data'}, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['DELETE'])
def product_delete(request):
  try:
    data = request.data
    product = Product.objects.get(id=data['id'])
    if product:
      product.delete()
      return Response( {'message':'Product Deleted'})
    else:
      return Response( {'error':'Product not found'}, status=status.HTTP_400_BAD_REQUEST)
  except:
    return Response( {'error':'Missing data'}, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['POST'])
def product_search(request):
  try:
    data = request.data
    products = Product.objects.filter(name__icontains=data["name"]).all()
    if products:
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response( {'error':'Product not found'}, status=status.HTTP_400_BAD_REQUEST)
  except:
    return Response( {'error':'Missing Required Data'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def product_category(request):
  try:
    data = request.data
    products = Product.objects.filter(category__icontains=data["category"]).all()
    if products:
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response( {'error':'Product not found'}, status=status.HTTP_400_BAD_REQUEST)
  except:
    return Response({"error":"Missing Required Data"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def product_brand(request):
  try:
    data = request.data
    products = Product.objects.filter(brand__icontains=data['brand']).all()
    if products:
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response( {'error':'Product not found'}, status=status.HTTP_400_BAD_REQUEST)
  except:
    return Response( {'error':'Incorrect Data'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def product_price(request):
  try:
    data = request.data
    products = Product.objects.filter(price__gte=data['min_price'], price__lte=data['max_price']).all()
    if products:
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response( {'error':'Product not found'}, status=status.HTTP_400_BAD_REQUEST)
  except:
    return Response( {'error':'Incorrect Data'}, status=status.HTTP_400_BAD_REQUEST)
  

  