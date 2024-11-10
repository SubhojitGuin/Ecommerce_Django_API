from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from user.models import *
from .models import *
from order.models import *
from .serializer import *
from django.db.models import Avg

# Create your views here.
@api_view(['GET'])
def product_list(request , user_id):
    wishlist = Wishlist.objects.filter(user=user_id).all()
    wishlist_ids = []
    if wishlist:
      for wish in wishlist:
          wishlist_ids.append(wish.product.id) 
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    prod_dict = serializer.data
    for prod in prod_dict:
      if prod['quantity'] > 0:
          prod['available'] = 'In stock'
      else:
          prod['available'] = 'Out of stock'
      
      if prod['id'] in wishlist_ids:
            prod['wishlist'] = True
      else:
         prod['wishlist'] = False
      rating = Review.objects.filter(product_id=prod['id']).aggregate(Avg('rating'))['rating__avg']
      prod['average_rating'] = rating if rating else 0
      prod['reviews'] = Review.objects.filter(product_id=prod['id']).count()
        
    return Response(prod_dict)

@api_view(['GET'])
def product_detail(request, product_id):
  try:
    product = Product.objects.get(id=product_id)
    if product:
        quantity = product.quantity
        if quantity == 0:
           available = "Out of stock"
        else:
           available = "In stock"
        serializer = ProductSerializer(product, many=False)
        data = serializer.data
        data['available'] = available
        rating = Review.objects.filter(product_id=product_id).aggregate(Avg('rating'))['rating__avg']
        data['average_rating'] = rating if rating else 0
        data['reviews'] = Review.objects.filter(product_id=product_id).count()
        return Response(data)
    else:
        return Response({'error':'Product not found'}, status=status.HTTP_200_OK)
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
      return Response( {'error':'Product not found'}, status=status.HTTP_200_OK)
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
      return Response( {'error':'Product not found'}, status=status.HTTP_200_OK)
  except:
    return Response( {'error':'Missing data'}, status=status.HTTP_400_BAD_REQUEST)
  
# @api_view(['POST'])
# def product_search(request):
#   try:
#     data = request.data
#     products = Product.objects.filter(name__icontains=data["name"]).all()
#     if products:
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#     else:
#         return Response( {'error':'Product not found'}, status=status.HTTP_200_OK)
#   except:
#     return Response( {'error':'Missing Required Data'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def product_search(request):
    try:
      data = request.data
      data = {k : v for k , v in data.items() if v}
      product_union = Product.objects.all()
      if "name" in data:
        products_by_name = Product.objects.filter(name__icontains=data["name"]).all()
        products_by_category = Product.objects.filter(category__icontains=data["name"]).all()
        products_by_brand = Product.objects.filter(brand__icontains=data["name"]).all()

        product_union = products_by_name.union(products_by_category, products_by_brand)
      
      if "min_price" in data and "max_price" in data:
          products_by_price = Product.objects.filter(price__range=(data["min_price"], data["max_price"])).all()
          product_union = product_union.intersection(products_by_price)
      if "brand" in data:
          products_by_new_brand = Product.objects.filter(brand__icontains=data["brand"]).all()
          product_union = product_union.intersection(products_by_new_brand)
      if "category" in data:
          products_by_new_category = Product.objects.filter(category__icontains=data["category"]).all()
          product_union = product_union.intersection(products_by_new_category)

      if product_union:
        serializer = ProductSerializer(product_union, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
      else:
        return Response( {'error':'Product not found'}, status=status.HTTP_200_OK)
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
        return Response( {'error':'Product not found'}, status=status.HTTP_200_OK)
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
        return Response( {'error':'Product not found'}, status=status.HTTP_200_OK)
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
        return Response( {'error':'Product not found'}, status=status.HTTP_200_OK)
  except:
    return Response( {'error':'Incorrect Data'}, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET'])
def product_rating(request , product_id , rating):
   try:
      review_objs = Review.objects.filter(product_id=product_id, rating=rating).all()
      if review_objs:
         serializer = ModifiedReviewSerializer(review_objs, many=True)
         return Response(serializer.data)         
      else:
         return Response({"error" : "No reviews found"}, status=status.HTTP_200_OK)
   except:
        return Response({"error" : "Missing Required Data"}, status=status.HTTP_400_BAD_REQUEST)
      
  
@api_view(['POST'])
def add_review(request):
  try:
    data = request.data
    user_id = data['user']
    product_id = data['product']
    order_obj_list = Order.objects.filter(user=user_id, payment_status=True).all()
    for item in order_obj_list:
      order_id = item.id
      orderitem_obj = OrderItem.objects.filter(order_id=order_id, product_id=product_id).first()
      if orderitem_obj:
        data['verified_purchase'] = True
      
    serializer = ReviewSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'info':"Review added successfully!!!"}, status=status.HTTP_201_CREATED)
    return Response({'error':'Incorrect Credentials'}, status=status.HTTP_400_BAD_REQUEST)
  except:
    return Response( {'error':'Incorrect Credentials'}, status=status.HTTP_400_BAD_REQUEST)
  

@api_view(['GET'])
def get_reviews(request, product_id):
  try:
    reviews = Review.objects.filter(product_id=product_id).all()
    serializer = ModifiedReviewSerializer(reviews, many=True)
    return Response(serializer.data)
  except:
    return Response( {'error':'No Reviews found'}, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_review(request, user_id, product_id):
  try:
    data = request.data
    review = Review.objects.get(user_id=user_id, product_id=product_id)
    if review:
        serializer = ReviewSerializer(review, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response({'message':'Review Updated'}, status=status.HTTP_200_OK)
    else:
      return Response( {'error':'Review not found'}, status=status.HTTP_200_OK)
  except:
    return Response( {'error':'Missing data'}, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['DELETE'])
def delete_review(request, user_id, product_id):
  try:
    review = Review.objects.get(user_id=user_id, product_id=product_id)
    if review:
      review.delete()
      return Response( {'message':'Review Deleted'})
    else:
      return Response( {'error':'Review not found'}, status=status.HTTP_200_OK)
  except:
    return Response( {'error':'Missing data'}, status=status.HTTP_400_BAD_REQUEST)