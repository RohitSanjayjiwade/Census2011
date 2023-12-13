# Generated by Django 4.2.8 on 2023-12-13 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0023_remove_city_slug_remove_village_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='village',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
