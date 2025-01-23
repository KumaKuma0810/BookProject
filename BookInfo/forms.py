from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User

from .models import *


class UserSignInForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользовтеля',  widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Адрес электронной почты',  widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'label': 'Пароль','class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )

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
        widgets = {
            'name_book': forms.TextInput(attrs={'class': 'form-control'}),            
            'avtor': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'year_of_publication': forms.DateInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'cover': forms.FileInput(),
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
    query = forms.CharField(label='', required=False, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

class ProfileForm(UserChangeForm):
    username = forms.CharField(label='Имя пользовтеля',  widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя пользовтеля',  widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Имя пользовтеля',  widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Имя пользовтеля',  widget=forms.EmailInput(attrs={'class': 'form-control'}))
    birthday = forms.DateField(label='Имя пользовтеля',  widget=forms.DateInput(attrs={'class': 'form-control'}))
    profile_picture = forms.ImageField(label='Аватар профиля',  widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta: 
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'email', 'birthday', 'profile_picture']

    