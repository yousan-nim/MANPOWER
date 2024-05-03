
import io, csv, pandas as pd

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework.parsers import  MultiPartParser
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import  BasePermission, IsAuthenticated, IsAdminUser, AllowAny

from drf_yasg.utils import swagger_auto_schema

from .models import ManpowerData
from .serializers import FileUpLoadSerializer, ManpowerDataSerializer


# CUSTOM PERMISSIONS FOR MANPOWER
class AdminManpowerPermissions(BasePermission):
    message = 'Admin Only'
    
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj): 
        return obj == request.user and request.user.is_staff
    
class LoggedInOrAdminManpowerPermissions(BasePermission):
    message = 'LoggedIn User or Admin'
    
    def has_object_permission(self, request, view, obj): 
        return obj == request.user or request.user.is_staff
    

# UPLOAD CSV FILE
class UploadFileView(generics.CreateAPIView): 
    serializer_class = FileUpLoadSerializer
    parser_classes = (MultiPartParser,)
    permission_classes = [AdminManpowerPermissions]
    
    @swagger_auto_schema(operation_description='Upload file...',)
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        
        while True:
            try:
                for idx, row in reader.iterrows():  
                    # The last row of csv always "" 
                    # Aoive to insert "" data record
                    if idx == len(reader) - 1:
                        break
                    
                    new_file = ManpowerData(
                        id             = int(row['_id']),
                        Seed_RepDate    = int(row['Seed_RepDate']),
                        Seed_Year       = int(row['Seed_Year']),
                        Seeds_YearWeek  = int(row['Seeds_YearWeek']),
                        Seed_Varity     = row['Seed_Varity'],
                        Seed_RDCSD      = row['Seed_RDCSD'],
                        Seed_Stock2Sale = row['Seed_Stock2Sale'],
                        Seed_Season     = int(row['Seed_Season']),
                        Seed_Crop_Year  = row['Seed_Crop_Year'],
                    )
                    new_file.save()
                    
                return Response({"Message": "Success to upload."}, status.HTTP_201_CREATED)
            
            except:
                return Response({"Message": "Fali to upload or Some record '_id' already import"}, status=status.HTTP_400_BAD_REQUEST)      


# READ ALL DATA
class DataAllView(APIView):
    # PERMISSIONS
    permission_classes = (IsAdminUser, )
    
    ################################################################################
    def get(self, request):
        data = ManpowerData.objects.all()
        serializers = ManpowerDataSerializer(data, many=True)
        if ManpowerData.DoesNotExist:    
            return Response(
                serializers.data, 
                status=status.HTTP_404_NOT_FOUND
            )
        return Response({"Message": "GET All Success", "data": serializers.data }, status=status.HTTP_200_OK)
    
    
# CRUD METHODS
class PostDataView(APIView):
    # PERMISSIONS
    permission_classes = (IsAuthenticated, )
    
    # CREATE DATA API
    ################################################################################
    def post(self, request):
        serializer = ManpowerDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "POST Success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({ "Message": "POST Failed", "data": serializer.errors }, status=status.HTTP_400_BAD_REQUEST)
    

class GetDataView(APIView):
    # PERMISSIONS
    permission_classes = (IsAuthenticated, )
    
    # GET DATA API
    ################################################################################
    def get(self, request, id):
        data = ManpowerData.objects.filter(id=id)
        serializers = ManpowerDataSerializer(data, many=True)
        return Response({ "Message": "GET Success", "data": serializers.data }, status=status.HTTP_200_OK)


class PatchDataView(APIView):
    # PERMISSIONS
    permission_classes = (IsAuthenticated, )
    
    # PATCH DATA API
    ################################################################################
    def patch(self, request, id): 
        data_get = ManpowerData.objects.get(id=id)  
        serializers = ManpowerDataSerializer(data_get, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({ "Message": "UPDATE Success", "data": serializers.data }, status=status.HTTP_200_OK)
        return Response({ "Message": "UPDATE Failed", "data": serializers.errors }, status=status.HTTP_400_BAD_REQUEST)
        
           
 
class DeleteDataView(APIView):
    # PERMISSIONS
    permission_classes = (IsAuthenticated, )
    
    # DELETE DATA API
    ################################################################################
    def delete(self, request, id): 
        data = ManpowerData.objects.get(id=id)
        data.delete()
        return Response({ "Message": "DELETE Success" }, status=status.HTTP_204_NO_CONTENT)
    
    
    
    
    
    
    
    