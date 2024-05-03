from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework.permissions import  AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .utils import get_tokens_for_user
from .serializers import RegistrationSerializer, UserTokenObtainPairSerializer, LoginSerializers

from django.contrib.auth import get_user_model

User = get_user_model()


# TOKEN    
class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer
    
    
# REGISTER
class RegistrationView(APIView):
    permission_classes = (AllowAny, )
    
    @swagger_auto_schema(request_body=RegistrationSerializer)
    def post(self, request, format=None):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# LOGIN
class LoginView(APIView): 
    permission_classes = (AllowAny, )
    
    # @swagger_auto_schema(request_body=LoginSerializers)
    def post(self, request, format=None): 
        if "email" not in request.data or "password" not in request.data: 
            return Response({'message': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
    
        email=request.data.get('email', None)
        password=request.data.get('password', None)
        
        print(email, password)

        user = authenticate(request, email=email, password=password)
        
        print(user)
        

        login(request, user)
        auth_data = get_tokens_for_user(request.user)
        return Response({**auth_data}, status=status.HTTP_200_OK)
        
        # if user is not None: 
        #     login(request, user)
        #     auth_data = get_tokens_for_user(request.user)
        #     return Response({**auth_data}, status=status.HTTP_200_OK)
            
        # return Response({'message': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
# LOGOUT
class LogoutView(APIView):
    permission_classes = (IsAuthenticated, )
    
    @swagger_auto_schema(request_body=LoginSerializers)
    def post(self, request, format=None):
        logout(request)
        return Response({'message': 'Successfully Logged out'}, status=status.HTTP_200_OK)
    
    
    