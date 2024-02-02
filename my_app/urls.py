from django.urls import path, include
# from .views import PostViewSet
from rest_framework.routers import DefaultRouter
from .views import (PostListAPIView,
                    PostDetailAPIView,
                    PostCreateAPIView,
                    PostUpdateAPIView,
                    PostDeleteAPIView,
                    PostListCreateAPIView,
                    PostUpdateRetrieveDestroyAPIView,
                    PostRetrieveDestroyAPIView)

# router = DefaultRouter()
# router.register('', PostViewSet, basename='posts')

urlpatterns = [
    # path('', include(router.urls))
    path('post/', PostListAPIView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('post/create/', PostCreateAPIView.as_view(), name='post-create'),
    path('post/update/<int:pk>/', PostUpdateAPIView.as_view(), name='post-update'),
    path('post/delete/<int:pk>/', PostDeleteAPIView.as_view(), name='post-delete'),
    path('post-list/', PostListCreateAPIView.as_view(), name='post-list-create'),
    path('post-detail/<int:pk>/', PostUpdateRetrieveDestroyAPIView.as_view(), name='post-rud'),
    path('kamoliddin/<int:pk>/', PostRetrieveDestroyAPIView.as_view(), name='post-detail-delete')
]
