from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


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
    query = forms.CharField(required=False, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))


