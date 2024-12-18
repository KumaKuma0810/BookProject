from django.shortcuts import render
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy

from .models import Book, Review, ReadListBook, User

def BookList(request): 
    books = Book.objects.all() 

    return render(request, 'BookInfo/book_list.html')

    # model = Book
    # template_name = 'BookInfo/book-list.html'
    # content_object_name = 'books'


# class BookDetailView(DetailView):
#     model = Book
#     template_name = 'BookInfo/book_detail.html'
#     content_object_name = 'book'


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