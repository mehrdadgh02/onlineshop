from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product,ProductCategory,ProductTag,ProductBrand
from .serializers import ProductSerializer,ProductBrandSerializer,ProductCategorySerializer,ProductTagSerializer

# Create your views here.
class ProductGenericApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(APIView):
   def get(self,request,Product_id):
       try:
           product = Product.objects.get(pk= Product_id)
           serializer = ProductSerializer(product)
           return Response(serializer.data)
       except Product.DoesNotExist:
           return Response(status=status.HTTP_404_NOT_FOUND)
class ProductCategoryGenericApiView(generics.ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class ProductTagGenericApiView(generics.ListAPIView):
    queryset = ProductTag.objects.all()
    serializer_class = ProductTagSerializer


class ProductBrandGenericApiView(generics.ListAPIView):
    queryset = ProductBrand.objects.all()
    serializer_class = ProductBrandSerializer