# Generated by Django 4.2.8 on 2023-12-13 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0026_city_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='slug',
        ),
    ]
