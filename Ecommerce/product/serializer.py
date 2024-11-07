from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
      model = Product
      fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
   class Meta:
       model = Review
       fields = '__all__'

class ModifiedReviewSerializer(serializers.ModelSerializer):

    user_name = serializers.CharField(source='user.first_name', read_only=True)
    
    class Meta:
        model = Review
        fields = ['user_name', 'rating', 'review','verified_purchase', 'created_at', 'updated_at']



   