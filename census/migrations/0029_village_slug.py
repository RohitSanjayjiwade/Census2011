# Generated by Django 4.2.8 on 2023-12-13 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0028_city_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='village',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]