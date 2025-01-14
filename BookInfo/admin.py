from django.contrib import admin
from .models import *
from django.utils.html import format_html

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'creation_at',
        'book'  
    )
    list_filter = ('username', 'creation_at')

    # def post_link(self, obj):
    #     return mark_safe(f'<a href="{obj.book.get_absolute_url()}">{obj.book.username} </a> ')


class ReadListBookAdmin(admin.ModelAdmin):
    list_display = (
        'list_name',
    )

    search_fields = ('list_name', 'list_name', 'books')



class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username', 
        'email'
    )

    search_fields = ('username', 'email')

class BookAdmin(admin.ModelAdmin):
    list_display = (
        'name_book',
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

admin.site.register(Review, ReviewAdmin)
admin.site.register(ReadListBook ,ReadListBookAdmin)
admin.site.register(Userdb, UserAdmin)
admin.site.register(Book, BookAdmin)