from django.urls import path
# from .views import UserDetailAPI,RegisterUserAPIView
from .views import ProductGenericApiView, ProductBrandGenericApiView, ProductCategoryGenericApiView,ProductTagGenericApiView, ProductDetailView

urlpatterns = [
  path('product/',ProductGenericApiView.as_view()),
  path('product_detail/',ProductDetailView.as_view()),
  path('',ProductBrandGenericApiView.as_view()),
  path('',ProductCategoryGenericApiView.as_view()),
  path('',ProductTagGenericApiView.as_view()),
]