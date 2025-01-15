from django.urls import path
from .views import *

urlpatterns = [
    # path('search/', SearchList, name='search'),
    path('', BookList, name='bookList'),
    # path('my-book/', MyBook, name='my-book'),
    path('bookAdd/', BookAdd, name='bookAdd'),
    path('about/', About, name='about'),
    path('book/<int:pk>/', BookDetail, name='bookDetail'),
    path('search/', SearchBooks, name='search'),
    path('favorites/', FavoritesBooks, name='favorites'),    
    # path('logout/', LogoutView, name='logout'),
    path('signup/', Signup, name='signup'),
    path('signin/', Singin, name='signin'),
    path('profile/', Profile, name='profile'),
    

    # path('book/<int:pk>/', BookDetailView(), name='book-detail'),
    # path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='book-edit'),
    # path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]