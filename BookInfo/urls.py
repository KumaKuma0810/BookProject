from django.urls import path
from .views import *

urlpatterns = [
    path('', BookList, name='book-list'),
    # path('book/<int:pk>/', BookDetailView(), name='book-detail'),
    # path('book/add/', BookCreateView.as_view(), name='book-add'),
    # path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='book-edit'),
    # path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]