# Generated by Django 5.0.6 on 2024-06-03 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0021_book_fiche_book_implutation_book_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='UAP',
            field=models.CharField(default='', max_length=100),
        ),
    ]