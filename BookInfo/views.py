from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator 
from django.contrib.auth import login, logout
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.urls import reverse_laz
from .models import *
from .forms import *


def About(request):
    return render(request, 'BookInfo/about.html')

def BookList(request): 
    object_list = Book.objects.all()  # Получаем все объекты модели
    paginator = Paginator(object_list, 6)  # 10 объектов на странице

    page_number = request.GET.get('page')  # Получаем номер страницы из URL
    page_obj = paginator.get_page(page_number)  # Получаем объекты для текущей страницы

    return render(request, 'BookInfo/book_list.html', {'object_list': object_list, 'page_obj': page_obj})

def BookAdd(request):
    if request.method == 'POST':
        form = AddBookForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Сохраняем новый продукт в базе данных
            return redirect('/')  # Перенаправление на страницу со списком продуктов
    else:
        form = AddBookForms()
    return render(request, 'BookInfo/book_add.html', {'form': form})

def BookDetail(request, pk):
    # post_book = Book.objects.filter(pk=id)
    book = get_object_or_404(Book, pk=pk)
    rating_book = Review.objects.all()
    
    if request.method == 'POST':
        book_form = CommentsForm(request.POST)

        if book_form.is_valid():
            comment = book_form.save(commit=False)
            comment.username = request.user
            comment.book = book_form
            parent_comm = request.POST.get('parent')
            
            if parent_comm:
                comment.parent = book_form.objects.get(id=parent_comm)
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        book_form = CommentsForm()

    return render(request, 'BookInfo/book_detail.html', {
        'rating_book': rating_book,
        'book': book,
    })

def SearchBooks(request):
    form = SearchForm(request.GET)
    
    if form.is_valid():
        query = form.cleaned_data['query']
        books_query = Book.objects.filter(name_book__exact=query)

    return render(request, 'BookInfo/search_list.html', {
        'book': books_query,
        'form': form,
    })


    
    # return render(request, 'BookInfo/template_tag/sigin_main.html', {'form': form})

def Signup(request):
    if request.method == 'POST':    
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account success!')
            
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

def EditProfile(request):
    if request.method == 'POST':
        # получаем профиль пользователя 
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return render('bookList')
    else:
        form = ProfileForm(instance=request.user)
    
    return render(request, 'BookInfo/profile.html', {'form': form})



    return render(request, 'BookInfo/profile.html', {'profile': profile})

def FavoritesBooks(request):    
    books = Book.objects.all()

    return render(request, 'BookInfo/favorites.html', {'books': books})

