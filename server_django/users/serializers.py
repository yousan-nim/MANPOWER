

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate


from django.contrib.auth.hashers import make_password
from .models import User


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token

class RegistrationSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ['email', 'password']

    def save(self):
        user = User(
            email=self.validated_data['email'], 
        )
        password = make_password(self.validated_data['password'])
        
        user.set_password(password)
        user.save()
        return user
    
class UserSerializer(ModelSerializer): 
    class Meta: 
        model = User 
        fields = ['id', 'email']    
    
class LoginSerializers(serializers.Serializer):
    password = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = User
        email = serializers.CharField(max_length=255)
        password = serializers.CharField(max_length=128, write_only=True)
