# Generated by Django 5.0.4 on 2024-05-05 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0009_remove_book_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='todo',
        ),
    ]
