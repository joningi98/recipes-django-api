# Generated by Django 4.0.3 on 2023-03-24 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_ingredient_recipe_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='recipe_id',
        ),
    ]
