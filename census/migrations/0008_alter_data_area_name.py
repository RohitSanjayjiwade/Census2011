# Generated by Django 4.2.8 on 2023-12-08 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0007_alter_district_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='area_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
