from rest_framework import serializers
from account_module.models import Register_User,Login_User


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register_User
        fields = '__all__'

class Login_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login_User
        fields = '__all__'