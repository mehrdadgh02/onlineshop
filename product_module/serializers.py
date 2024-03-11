from rest_framework import serializers
from .models import Product,ProductCategory,ProductTag,ProductBrand


class ProductSerializer(serializers.ModelSerializer):
  class Meta:
     model = Product
     fields = '__all__'

class ProductCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = ProductCategory
    fields = '__all__'

class ProductTagSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProductTag
    fields = '__all__'

class ProductBrandSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProductBrand
    fields = '__all__'