from django.urls import path
from . import views
from .views import ( 
    UserTokenObtainPairView, 
    RegistrationView , 
    LoginView, 
    LogoutView, 

)

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('token/', UserTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]