from django.urls import path

from .views import (
    # UPLOAD CSV FILE
    UploadFileView, 
    
    # CRUD METHODS
    DataAllView, 
    PostDataView, 
    GetDataView, 
    PatchDataView, 
    DeleteDataView
)


urlpatterns = [
    # UPLOAD CSV FILE
    path('upload/', UploadFileView.as_view() , name='upload-file'),
    
    # CRUD METHODS
    path('get-all/', DataAllView.as_view() , name='get-all'),
    path('post-data/', PostDataView.as_view() , name='post-data'),
    # PATCH METHODS NEEDb PRIMARY KEY ID 
    path('get-data/<int:id>', GetDataView.as_view() , name='get-data'),
    path('patch-data/<int:id>', PatchDataView.as_view() , name='patch-data'),
    path('delete-data/<int:id>', DeleteDataView.as_view() , name='delete-data'),
    
]



