from django.shortcuts import render, redirect
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy

from .models import *
from .forms import AddBookForms

def About(request):
    return render(request, 'BookInfo/about.html')

def BookList(request): 
    books = Book.objects.all() 

    return render(request, 'BookInfo/book_list.html', {'books': books})

def BookAdd(request):
    if request.method == 'POST':
        form = AddBookForms(request.POST)

        if form.is_valid():
            form = form.save()
        #   book = Book.objects.create(**form.cleaned_data)
            return redirect('/')
    else:
        form = AddBookForms()

    return render(request, 'BookInfo/book_add.html', {'form': form})

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