from django import forms


class AddBookForms(forms.Form):
    name = forms.CharField(max_length=200, label='Название книги', required=True)
    avtor = forms.CharField(max_length=200, label='Автор', required=True)
    genre = forms.CharField(max_length=200, label='Жанр', required=True)
    year_of_publication = forms.DateField(required=False, label='Дата публикации книги', widget=forms.DateInput(attrs={'type': 'date'} ))
    description = forms.CharField(max_length=200, label='Описание', required=True, widget=forms.Textarea)
    cover = forms.ImageField(label='Обложка', required=False, widget=forms.FileInput)

    