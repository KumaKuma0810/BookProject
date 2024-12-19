from django.shortcuts import render, redirect
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy

from .models import *
from .forms import AddBookForms

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


def BookAdd(request):
    if request.method == 'POST':
        form = AddBookForms(request.POST, request.FILES)

        if form.is_valid():
            name = form.cleaned_data['name']
            avtor = form.cleaned_data['avtor']
            genre = form.cleaned_data['genre']
            year_of_publication = form.cleaned_data['year_of_publication']
            description = form.cleaned_data['description']
            cover = form.cleaned_data['cover']

            return redirect('book-list')
        else:
            return HttpResponse('Invalid data')
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