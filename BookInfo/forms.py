from django import forms

from .models import Book

# class AddBookForms(forms.Form):
#     username = forms.CharField(max_length=200, label='Название книги', required=True, widget=forms.TextInput())
#     avtor = forms.CharField(max_length=200, label='Автор', required=True)
#     genre = forms.CharField(max_length=200, label='Жанр', required=True)
#     year_of_publication = forms.DateField(required=False, label='Дата публикации книги', widget=forms.DateInput(attrs={'type': 'date'} ))
#     description = forms.CharField(max_length=200, label='Описание', required=True, widget=forms.Textarea)
#     cover = forms.ImageField(label='Обложка', required=False, widget=forms.FileInput)

class AddBookForms(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = [
            'username',
            'avtor',
            'genre',
            'year_of_publication',
            'description',
            'cover'
        ]
        widget = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),            
            'avtor': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'year_of_publication': forms.DateInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'rows': 5, 'class': 'form-control'}),
            'cover': forms.FileInput(attrs={'class': 'form-control'}),
        }