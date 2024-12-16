from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = (
        'username', 
        'avtor', 
        'genre', 
        'year_of_publication', 
        'description', 
        'cover', 
        'date_added'
    )

    search_fields = ('username', 'avtor', 'genre', 'date_added')
    ordering = ('date_added',)

admin.site.register(Book, BookAdmin)

