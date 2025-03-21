# Generated by Django 5.1.6 on 2025-03-17 21:11

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя автора')),
                ('bio', models.TextField(blank=True, max_length=455, verbose_name='О авторе')),
                ('img_author', models.ImageField(blank=True, default='/upload/Author/default.jpg', max_length=255, upload_to='upload/Author/', verbose_name='Фото автора')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=20, verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_book', models.CharField(max_length=100, verbose_name='Название книги')),
                ('description', models.TextField(verbose_name='Описание')),
                ('cover', models.ImageField(blank=True, default='/upload/Book/Image-not-found.png', upload_to='upload/Book/', verbose_name='Обложка книги')),
                ('date_added', models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='Дата добавления')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookInfo.author')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookInfo.genre')),
            ],
            options={
                'verbose_name': 'Книги',
                'verbose_name_plural': 'Книги',
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст отзыва')),
                ('creation_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookInfo.book', verbose_name='Книга')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['-creation_at'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField(blank=True, null=True)),
                ('profile_picture', models.ImageField(default='upload/Users/avatar_default.png', null=True, upload_to='upload/Users/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookInfo.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Избранное')),
            ],
            options={
                'unique_together': {('user', 'book')},
            },
        ),
    ]
