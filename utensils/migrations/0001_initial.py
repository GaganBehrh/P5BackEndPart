# Generated by Django 3.2 on 2023-03-28 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='utensils',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spoon', models.CharField(max_length=255)),
                ('plate', models.CharField(max_length=255)),
                ('cup', models.CharField(max_length=255)),
            ],
        ),
    ]
