from django.db import models
from django.utils import timezone

class User(models.Model):                   # пользователь
    username = models.CharField(verbose_name='Имя пользователя', max_length=20)
    email = models.EmailField(verbose_name='Почта пользователя', unique=True, )


    def __str__(self):
        return self.username


class Book(models.Model):                   # книга
    username = models.CharField(verbose_name='Название книги', max_length=100)
    avtor = models.CharField(verbose_name='Автор', max_length=100)
    genre = models.CharField(verbose_name='Жанр', max_length=20)
    year_of_publication = models.DateField(verbose_name='Дата публикации книги', blank=False)
    description = models.TextField(verbose_name='Описание', blank=False)
    cover = models.ImageField(upload_to='upload/Book/', max_length=100, verbose_name='Обложка книги', unique=True, blank=True, default='upload/BookInfo/default.jpg')
    date_added = models.DateField(verbose_name='Дата добавления', default=timezone.now, blank=True)

    def __str__(self):
        return self.username
    

class Review(models.Model):                 # отзыв
    text = models.TextField(verbose_name='Текст отзыва')
    rating = models.IntegerField(verbose_name='Рейтинг')
    creation_date = models.DateField(auto_created=True, verbose_name='Дата создания')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.username.username}'


class ReadListBook(models.Model):          # список чтения
    list_name = models.CharField(verbose_name='список книг', max_length=20)
    user = models.CharField(verbose_name='пользователь', max_length=10)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.user