# Generated by Django 5.1.4 on 2024-12-16 14:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookInfo', '0002_alter_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='username',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='BookInfo.user'),
            preserve_default=False,
        ),
    ]