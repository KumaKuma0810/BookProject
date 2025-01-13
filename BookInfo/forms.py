from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import *

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
            'name_book',
            'avtor',
            'genre',
            'year_of_publication',
            'description',
            'cover'
        ]
        widget = {
            'name_book': forms.TextInput(attrs={'class': 'form-control'}),            
            'avtor': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'year_of_publication': forms.DateInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'rows': 5, 'class': 'form-control'}),
            'cover': forms.FileInput(attrs={'class': 'form-control'}),
        }


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'creation_at', 'rating', 'username', 'book', 'parent']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'parent' in self.fields:
            self.fields['parent'].required = False
        

class SearchForm(forms.Form):
    query = forms.CharField(required=False, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))


class SignForm(forms.ModelForm):
    username = forms.CharField(required=True, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Имя пользователя')
    password = forms.CharField(required=True, max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Пароль')
    password1 = forms.CharField(required=True, max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Повторите пароль')
    email = forms.CharField(required=True, max_length=255, widget=forms.EmailInput(attrs={'class': 'form-control'}), label='Почта')

    class Meta:
        model = User 
        fields = ['username', 'password', 'password1', 'email']

    # def clean_field(self):
        # cleaned_data = super().clean()
        # password = cleaned_data('password')
        # password1 = cleaned_data('password1')
        
        # if password is not password1:
        #     raise ValidationError('Пароли не совпадают !')
        # return cleaned_data







# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=255, label='Логин')
#     password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

#     def clean(self):
#         cleaned_data = super().clean()
#         username = cleaned_data['username']
#         password = cleaned_data['password']
#         user = authenticate(username=username, password=password)

#         if user in None:
#             raise forms.ValidationError('Неверный логин или пароль')

#         cleaned_data['user'] = user
#         return cleaned_data
    



    
