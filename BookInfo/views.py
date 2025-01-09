from django.shortcuts import render, redirect, get_object_or_404
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy

from .models import *
from .forms import *


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