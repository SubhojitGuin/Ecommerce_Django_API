from rest_framework import serializers
from .models import *

#Coverts our models to json objects
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'