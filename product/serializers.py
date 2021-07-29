from rest_framework import serializers
from .models import Products, ProductType

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ('__all__')

class ProductSerializer(serializers.ModelSerializer):
    product_type = ProductTypeSerializer(read_only=True)
    class Meta:
        model = Products
        fields = '__all__'