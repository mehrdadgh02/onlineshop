from django.shortcuts import render
from rest_framework import generics
from .models import Register_User, Login_User
from .serializers import  RegisterUserSerializer, Login_UserSerializer

# Create your views here.
class RegisterUserGenericApiView(generics.CreateAPIView):
    queryset = Register_User.objects.all()
    serializer_class = RegisterUserSerializer

class Login_UserSerializerGenericApiView(generics.ListAPIView):
    queryset = Login_User.objects.all()
    serializer_class = Login_UserSerializer