# Generated by Django 2.2.24 on 2021-07-26 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20210726_1005'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='favoritemovies',
            table='Favorite_Movies',
        ),
    ]
