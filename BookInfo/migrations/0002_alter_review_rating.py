# Generated by Django 5.1.4 on 2024-12-16 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookInfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(verbose_name='Рейтинг'),
        ),
    ]