from django.urls import path
from .views import (BooksListCreateAPIView,
                    BooksUpdateRetrieveDestroyAPIView)

urlpatterns = [
    path('books/', BooksListCreateAPIView.as_view(), name='books_list_create'),
    path('books/<int:pk>/', BooksUpdateRetrieveDestroyAPIView.as_view(), name='books_update_retrieve')
]