from django.urls import path
# from .views import UserDetailAPI,RegisterUserAPIView
from .views import RegisterUserAPIView
urlpatterns = [
  # path('get_details/',UserDetailAPI.as_view()),
  path('register/',RegisterUserAPIView.as_view()),
]