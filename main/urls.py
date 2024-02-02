from django.urls import path
from .views import (getApiView,
                    createApiView,
                    updateApiView,
                    deleteApiView,
                    detailApiView)

urlpatterns = [
    path('get/', getApiView, name = 'get'),
    path('create/', createApiView, name = 'create'),
    path("get/<int:pk>/update/", updateApiView, name = 'update'),
    path("<int:pk>/delete/", deleteApiView, name = 'delete'),
    path("<int:pk>/detail/", detailApiView, name = 'detail')
]