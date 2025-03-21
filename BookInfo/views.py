from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator 
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.urls import reverse_laz
from .models import *
from .forms import *


@login_required
def SearchGenre(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    genre_book = Book.objects.filter(genre__genre_name=genre)

    return render(request, 'BookInfo/resultGen.html', {'genre_book': genre_book})


@login_required
def SearchAuthor(request, author_id):
    author = Book.objects.filter(author=author_id)

    return render(request, 'BookInfo/resultAuthor.html', {'author': author})


@login_required
def Logout(request):
    logout(request)
    return redirect('bookList')


def About(request):
    return render(request, 'BookInfo/about.html')


def BookList(request): 
    object_list = Book.objects.all()  # Получаем все объекты модели
    paginator = Paginator(object_list, 6)  # 10 объектов на странице

    page_number = request.GET.get('page')  # Получаем номер страницы из URL
    page_obj = paginator.get_page(page_number)  # Получаем объекты для текущей страницы

    return render(request, 'BookInfo/book_list.html', {
        'object_list': object_list, 
        'page_obj': page_obj,
        }
    )

def BookAdd(request):
    genre = Genre.objects.all()
    author = Author.objects.all()

    if request.method == 'POST':
        form = AddBookForms(request.POST, request.FILES)
        if form.is_valid():
            name_book = form.cleaned_data['name_book']
            author = form.cleaned_data['author']
            genre = form.cleaned_data['genre']
            description = form.cleaned_data['description']
            cover = form.cleaned_data['cover']
            form.save()

            return redirect('bookList')  # Перенаправление на страницу со списком продуктов
    else:
        form = AddBookForms()

    return render(request, 'BookInfo/book_add.html', {
        'form': form, 
        'genre': genre,
        'author': author
    })


def BookDetail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    comments = Comment.objects.filter(book=book)
    recommendations = Book.objects.filter(genre=book.genre).exclude(id=book.id)[:3]

    if request.user.is_authenticated:
        favorite, created = Favorite.objects.get_or_create(user=request.user, book=book)
    else:
        created = False

    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment, created = Comment.objects.get_or_create(
                book=book,
                username=request.user,
                text=form.cleaned_data['text']
            )
            return redirect('bookDetail', book_id=book.id)
    else:
        form = CommentsForm()

    return render(request, 'BookInfo/book_detail.html', {
        'recommendations': recommendations,
        'book': book,
        'created': created,
        'form': form,
        'comments': comments,
    })


@login_required
def DeleteComment(request, comm_id):
    comment = get_object_or_404(Comment, id=comm_id)

    if request.user.is_superuser or request.user == comment.username :
        comment.delete()
    
    return redirect(request.META.get('HTTP_REFERER', '/'))

    
def SearchBooks(request):
    form = SearchForm(request.GET)
    
    if form.is_valid():
        query = form.cleaned_data['query']
        books_query = Book.objects.filter(name_book__exact=query)

    return render(request, 'BookInfo/search_list.html', {
        'book': books_query,
        'form': form,
    })


def Signup(request):
    if request.method == 'POST':    
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)

            if hasattr(user, 'profile'):
                user.profile.profile_picture = request.user.profile.profile_picture
                user.profile.birthday = request.user.profile.birthday
                user.profile.save()
            else: 
                Profile.objects.create(user=user)

            return redirect('bookList')
        else:
            messages.error(request, 'Error account!')
    else:
        form = UserRegisterForm()

    return render(request, 'BookInfo/signup.html', {'form': form})


def Singin(request):
    if request.method == 'POST':
        form = UserSignInForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('bookList')
    else:
        form = UserSignInForm()
    return render(request, 'BookInfo/signin.html', {'form': form})


@login_required
def EditProfile(request):
    if request.method == 'POST': 
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():            
            user_form.save()
            profile_form.save()
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'BookInfo/profile.html', {'user_form': user_form, 'profile_form': profile_form})

# Favorite
@login_required
def FavoritesListBooks(request):    
    favorites = Favorite.objects.filter(user=request.user).select_related('book')
    return render(request, 'BookInfo/favorites.html', {'favorites': favorites})


@login_required
def AddFavorites(request, pk):
    book = get_object_or_404(Book, id=pk)
    # Проверяем, есть ли уже эта книга в избранном у пользователя
    favorite, created = Favorite.objects.get_or_create(user=request.user, book=book)
    return redirect('favorites')

@login_required
def RemoveFromFavorites(request, id):
    favorite = get_object_or_404(Favorite, user=request.user, book_id=id)
    favorite.delete()
    return redirect('favorites')



