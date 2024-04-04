from urllib import request

from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from .models import Product, ProductCategory, ProductTag, ProductBrand, Order_Product
from .serializers import ProductSerializer, ProductBrandSerializer, ProductCategorySerializer, ProductTagSerializer,OrderProductSerializer



# Create your views here.
class ProductGenericApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(APIView):
    def get(self, request, Product_id):
        try:
            product = Product.objects.get(pk=Product_id)
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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def order_product(request):
    product = request.data.get('product')
    delivery_time = request.data.get('delivery_time')
    receiver_info = request.data.get('receiver_info')
    
    order_product.objects.create(product=product, delivery_time=delivery_time, receiver_info=receiver_info)

    return Response({"message": "محصول با موفقیت به سبد خرید اضافه شد"}, status=status.HTTP_201_CREATED)

