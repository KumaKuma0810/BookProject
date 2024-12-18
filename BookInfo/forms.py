from django import forms


class AddBookForms(forms.Form):
    name = forms.CharField()
    avtor = forms.CharField()
    genre = forms.CharField()
    year_of_publication = forms.DateField()
    description = forms.TextField()
    cover = forms.ImageField()

    