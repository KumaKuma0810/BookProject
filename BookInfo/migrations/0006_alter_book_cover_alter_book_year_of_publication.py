# Generated by Django 5.1.4 on 2024-12-19 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookInfo', '0005_alter_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, default='upload/BookInfo/default.jpg', unique=True, upload_to='upload/Book/', verbose_name='Обложка книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year_of_publication',
            field=models.DateField(verbose_name='Дата публикации книги'),
        ),
    ]
