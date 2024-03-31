from django.urls import path
# from .views import UserDetailAPI,RegisterUserAPIView
from .views import ProductGenericApiView, ProductBrandGenericApiView, ProductCategoryGenericApiView, \
    ProductTagGenericApiView, ProductDetailView, order_product

urlpatterns = [
    path('product/', ProductGenericApiView.as_view()),
    path('product_detail/<int:pk>', ProductDetailView.as_view()),
    path('product/brand/', ProductBrandGenericApiView.as_view()),
    path('product/category/', ProductCategoryGenericApiView.as_view()),
    path('product/tag/', ProductTagGenericApiView.as_view()),
    path('product/order/', order_product),
]
