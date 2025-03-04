from django.contrib import admin
from django.utils.html import format_html

from .models import *

class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre_name',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio', 'img_author')
    search_fields = ('name',)

    def display_image(self, obj):
        if obj.img_author:
            return format_html('<img src="{}" style="width: 100px; height: 100px; border: 1px solid #ccc;" />', obj.img_author.url)



class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'creation_at',
        'book'  
    )

class ReadListBookAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'book'
    )

    search_fields = ('list_name',)



class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'birthday', 
        'profile_picture'
    )

    def display_image(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" style="width: 100px; height: 100px; border: 1px solid #ccc;" />', obj.profile_picture.url)


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'name_book',
        'author', 
        'genre', 
        'date_added',
        'display_image',
    )

    def display_image(self, obj):
        if obj.cover:
            return format_html('<img src="{}" style="width: 100px; height: 100px; border: 1px solid #ccc;" />', obj.cover.url)


    search_fields = ('author', 'genre', 'date_added')
    ordering = ('date_added',)

admin.site.register(Genre, GenreAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Favorite ,ReadListBookAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Book, BookAdmin)