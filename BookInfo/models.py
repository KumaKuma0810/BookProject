from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):                #Профиль пользователя
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='upload/Users/', default='upload/Users/avatar_default.png', blank=False, null=True)
    

    def __str__(self):
        return f"{self.user.username}'s profile"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

class Author(models.Model):
    name = models.CharField(verbose_name='Имя автора', max_length=255)
    bio = models.TextField(verbose_name='О авторе', max_length=455, blank=True)
    img_author = models.ImageField(upload_to='upload/Author/', max_length=255, verbose_name='Фото автора', unique=False, blank=True, default='/upload/Author/default.jpg')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name

class Genre(models.Model):
    genre_name = models.CharField(verbose_name='Жанр', max_length=20)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.genre_name



class Book(models.Model):                   # книга
    name_book = models.CharField(verbose_name='Название книги', max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание', blank=False)
    cover = models.ImageField(upload_to='upload/Book/', max_length=100, verbose_name='Обложка книги', unique=False, blank=True, default='/upload/Book/Image-not-found.png')
    date_added = models.DateField(verbose_name='Дата добавления', default=timezone.now, blank=True)

    
    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'Книги'
        ordering = ['-date_added']
    
    def __str__(self):
        return self.name_book


class Comment(models.Model):                 # отзыв
    text = models.TextField(verbose_name='Текст отзыва')
    creation_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания', unique=False)
    username = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')

    def __str__(self):
        return f'Comments by {self.username.username} on {self.book.name_book}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-creation_at']


class Favorite(models.Model):          # список чтения
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Избранное')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} - {self.book.name_book}'

    class Meta:
        unique_together = ('user', 'book')



