# Generated by Django 5.0.6 on 2024-06-03 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0022_book_uap'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='time_difference',
            field=models.CharField(default='00:00', max_length=12),
        ),
    ]
