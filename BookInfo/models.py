from django.db import models


class User(models.Model):                   # пользователь
    username = models.CharField(verbose_name='Имя пользователя', max_length=20)
    email = models.EmailField(verbose_name='Почта пользователя', unique=True, )


    def __str__(self):
        return self.username


class Book(models.Model):                   # книга
    username = models.CharField(verbose_name='Название книги', max_length=20)
    avtor = models.CharField(verbose_name='Автор', max_length=10)
    genre = models.CharField(verbose_name='Жанр', max_length=20)
    year_of_publication = models.DateField(verbose_name='Дата публикации', auto_now=False)
    description = models.TextField(verbose_name='Описание')
    cover = models.ImageField(upload_to='upload/Book/', max_length=100, verbose_name='Обложка книги')
    date_added = models.DateField(auto_created=True, verbose_name='Дата добавления')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

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