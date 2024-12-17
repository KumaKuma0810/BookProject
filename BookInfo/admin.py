from django.contrib import admin
from .models import *

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'creation_date',
        'book'        
    )

class ReadListBookAdmin(admin.ModelAdmin):
    list_display = (
        'list_name',
    )

    search_fields = ('list_name', 'list_name', 'books')

class BookAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'avtor', 
        'genre', 
        'date_added'
    )

    search_fields = ('avtor', 'genre', 'date_added')
    ordering = ('date_added',)

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username', 
        'email'
    )

    search_fields = ('username', 'email')

admin.site.register(Review, ReviewAdmin)
admin.site.register(ReadListBook ,ReadListBookAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(User, UserAdmin)
