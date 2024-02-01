from django.urls import path
from .views import (CreateAPIView,
                    UpdateRetrieveDestroyAPIView)

urlpatterns = [
    path('path/', CreateAPIView.as_view(), name='List_Create'),
    path('path/<int:pk>/', UpdateRetrieveDestroyAPIView.as_view(), name='Update_Retrieve')
]
