# Generated by Django 5.0.6 on 2024-05-31 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0018_book_conforme'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_confrome',
            field=models.BooleanField(default=False),
        ),
    ]
