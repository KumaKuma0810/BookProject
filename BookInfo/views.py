from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator 
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


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['comment_form'] = CommentsForm()
    #     return context



    return render(request, 'BookInfo/book_detail.html', {'book': book})

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
            messages.success(request, 'Account success!')
            # login(request, user)
            # return redirect('2')
        else:
            messages.error(request, 'Error account!')
    else:
        form = UserRegisterForm()

    return render(request, 'BookInfo/signup.html', {'form': form})



def Login(request):
    pass

def Singin(request):
    pass

# class BookCreateView(CreateView):
#     model = Book
#     template_name = 'BookInfo/book_add.html'
#     fields = [
#         'username', 
#         'avtor', 
#         'genre', 
#         'year_of_publication', 
#         'description', 
#         'cover', 
#         'date_added']
#     book_url = reverse_lazy('book-add')
    

# class BookUpdateView(UpdateView):
#     model = Book
#     tempalate_name = 'BookInfo/book_form.html'
#     fields = [
#         'username', 
#         'avtor', 
#         'genre', 
#         'year_of_publication', 
#         'description', 
#         'cover', 
#         'date_added']
#     success_url = reverse_lazy('book-edit')


# class BookDeleteView(DeleteView):
#     model = Book
#     template_name = 'book_confirm_delete.html'
#     success_url = reverse_lazy('book-delete')