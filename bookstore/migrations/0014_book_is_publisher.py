# Generated by Django 5.0.6 on 2024-05-29 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0013_book_controle_book_time2'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_publisher',
            field=models.BooleanField(default=False),
        ),
    ]