from django.urls import path
from .views import *

urlpatterns = [
    path('', BookList, name='bookList'),
    path('bookAdd/', BookAdd, name='bookAdd'),
    path('about/', About, name='about'),
    path('book/<int:book_id>/', BookDetail, name='bookDetail'),
    path('search/', SearchBooks, name='search'),

    path('favorites/', FavoritesListBooks, name='favorites'), 
    path('favorites/<int:pk>', AddFavorites, name='addFavorites'),  
    path('delete_book/<int:id>', RemoveFromFavorites, name='removeFromFavorites'),  
     
    path('signup/', Signup, name='signup'),
    path('signin/', Singin, name='signin'),
    path('logout/', Logout, name='logout'),
    path('profile/', EditProfile, name='profile'),
    

    # path('book/<int:pk>/', BookDetailView(), name='book-detail'),
    # path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='book-edit'),
    # path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]