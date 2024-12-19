from django.contrib import admin
from .models import *
from django.utils.html import format_html

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
        'date_added',
        'display_image',
    )

    def display_image(self, obj):
        if obj.cover:
            return format_html('<img src="{}" style="width: 100px; height: 100px; border: 1px solid #ccc;" />', obj.cover.url)


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
