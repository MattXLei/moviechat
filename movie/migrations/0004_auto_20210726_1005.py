# Generated by Django 2.2.24 on 2021-07-26 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20210725_1506'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='favoritemovies',
            table='favorite_movies',
        ),
    ]
