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

class ProfileUpdateForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, label='Аватарка',widget=forms.FileInput(attrs={"type":"file", "class":"custom-file-input", "id":"validatedCustomFile"}))
    birthday = forms.DateField(required=False, label='Дата рождения', widget=forms.DateInput(attrs={"type":"date", "id":"dateInput", "class":"form-control"}))

    class Meta:
        model = Profile
        fields = ['birthday', 'profile_picture']


class AddBookForms(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = [
            'name_book',
            'author',
            'genre',
            'description',
            'cover'
        ]
        # widgets = {
        #     'name_book': forms.TextInput(attrs={'class': 'form-control'}),            
        #     'author': forms.TextInput(attrs={'class': 'form-select',}),
        #     'genre': forms.TextInput(attrs={'class': 'form-select', 'id':'exampleSelect'}),
        #     'description': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
        #     'cover': forms.FileInput(),
        # }

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class SearchForm(forms.Form):
    query = forms.CharField(label='', required=False, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label='Имя',  widget=forms.TextInput(attrs={"type":"text", "id":"textInput", "class":"form-control"}))
    email = forms.CharField(label='Почта',  widget=forms.TextInput(attrs={ "type":"email" , "id":"exampleInputEmail1", "aria-describedby":"emailHelp", "placeholder":"Enter email", 'class': 'form-control'}))
   
    class Meta:
        model = User
        fields = ['username', 'email']


    