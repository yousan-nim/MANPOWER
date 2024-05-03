from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from .models import ManpowerData

# FILE UPLOAD MODELS
class FileUpLoadSerializer(Serializer):
    file = serializers.FileField()
    
class SaveFileUpLoadSerializer(Serializer):
    class Meta: 
        model = ManpowerData
        fields = '__all__'

class ManpowerDataSerializer(ModelSerializer):
    class Meta: 
        model = ManpowerData
        fields = '__all__'