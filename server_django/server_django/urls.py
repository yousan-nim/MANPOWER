
from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from rest_framework.permissions import IsAdminUser
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(IsAdminUser, ),
)

urlpatterns = [
   
   # API DOCUMENT SWAGGER
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
    # API APP
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('manpower/',  include('manpower.urls')),
    
    # Browable 
    path('api-auth/', include('rest_framework.urls')),
]
