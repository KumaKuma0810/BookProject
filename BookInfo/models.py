from django.db import models
from django.utils import timezone



class Userdb(models.Model):                   # пользователь
    username = models.CharField(verbose_name='Имя пользователя', max_length=20)
    # phone = models.IntegerField(verbose_name='Номер телефона', blank=True)
    # date_birthday = models.DateField(verbose_name='Дата рождения')
    email = models.EmailField(verbose_name='Почта пользователя', max_length=255)
    avatar = models.ImageField(upload_to='upload/Users/Avatar/', verbose_name='Аватарка', blank=True, default='/upload/Users/Avatar/avatar_default.png')

    def __str__(self):
        return self.username
            
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Book(models.Model):                   # книга
    name_book = models.CharField(verbose_name='Название книги', max_length=100)
    avtor = models.CharField(verbose_name='Автор', max_length=100)
    genre = models.CharField(verbose_name='Жанр', max_length=20)
    year_of_publication = models.DateField(verbose_name='Дата публикации книги', blank=False)
    description = models.TextField(verbose_name='Описание', blank=False)
    cover = models.ImageField(upload_to='upload/Book/', max_length=100, verbose_name='Обложка книги', unique=False, blank=True, default='/upload/Book/Image-not-found.png')
    date_added = models.DateField(verbose_name='Дата добавления', default=timezone.now, blank=True)

    
    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'Книги'
        ordering = ['-date_added']
    
    def __str__(self):
        return self.name_book



class Review(models.Model):                 # отзыв
    text = models.TextField(verbose_name='Текст отзыва')
    creation_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания', unique=False, blank=False)
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    username = models.ForeignKey(Userdb, on_delete=models.CASCADE, verbose_name='Пользователь')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')

    # def get_average_rating(self):
    #     ratings = self.book.rating.all()

    #     if ratings:
    #         total_score = sum([self.rating for rating in ratings])

    #         return total_score / len(ratings)
    #     return 0

    def __str__(self):
        return f'Comments by {self.username.username} on {self.book.name_book}'

    def get_replies(self):
        return self.get_replies.all().order_by('created_at')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        unique_together = ('book', 'username')  # Один пользователь может оценить продукт только один раз
        ordering = ['creation_at']



class ReadListBook(models.Model):          # список чтения
    list_name = models.CharField(verbose_name='список книг', max_length=20)
    user = models.CharField(verbose_name='пользователь', max_length=10)
    books = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


