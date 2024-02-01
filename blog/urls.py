from django.urls import path
from .views import (CreateAPIView,
                    UpdateRetrieveDestroyAPIView)

urlpatterns = [
    path('main/', CreateAPIView.as_view(), name='List_Create'),
    path('main/<int:pk>/', UpdateRetrieveDestroyAPIView.as_view(), name='Update_Retrieve')
]
