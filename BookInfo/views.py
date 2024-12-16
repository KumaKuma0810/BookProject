from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import *

class BookListView(ListView):
    model = Book
    template_name = 'book-list.html'
    content_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    content_object_name = 'book'


class BookCreateView(CreateView):
    model = Book
    template_name = 'book_form.html'
    fields = [
        'username', 
        'avtor', 
        'genre', 
        'year_of_publication', 
        'description', 
        'cover', 
        'date_added']
    book_url = reverse_lazy('book-list')
    

class BookUpdateView(UpdateView):
    model = Book
    tempalate_name = 'book_form.html'
    fields = [
        'username', 
        'avtor', 
        'genre', 
        'year_of_publication', 
        'description', 
        'cover', 
        'date_added']
    success_url = reverse_lazy('book-list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book-list')