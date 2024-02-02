from django.urls import path
from .views import home_page, post_list_api_view, post_api_view, put_api_view, delete_api_view

urlpatterns = [
    path('', home_page, name='home'),
    path('get/', post_list_api_view, name='post-list'),
    path('post/', post_api_view, name='post-list'),
    path('get/<int:pk>/', put_api_view, name='put-list'),
    path('delete/<int:pk>/', delete_api_view, name='delete')

]
