# Generated by Django 3.2 on 2023-03-17 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RecipeComment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipecomment',
            old_name='user',
            new_name='owner',
        ),
    ]
