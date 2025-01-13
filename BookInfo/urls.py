from django.urls import path
from .views import *

urlpatterns = [
    # path('search/', SearchList, name='search'),
    path('', BookList, name='book-list'),
    # path('my-book/', MyBook, name='my-book'),
    path('book/add/', BookAdd, name='book-add'),
    path('about/', About, name='about'),
    path('book/<int:pk>/', BookDetail, name='book_detail'),
    path('search/', SearchBooks, name='search'),

    
    # path('logout/', LogoutView, name='logout'),
    path('signup/', Signup, name='signup'),
    path('login/', Login, name='login'),

    # path('book/<int:pk>/', BookDetailView(), name='book-detail'),
    # path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='book-edit'),
    # path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]