# Generated by Django 5.0.6 on 2024-06-06 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0025_alter_book_fiche_alter_book_implutation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='produit',
            field=models.CharField(default='1', max_length=100),
        ),
    ]
