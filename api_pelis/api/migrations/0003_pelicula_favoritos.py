# Generated by Django 3.2.14 on 2023-03-28 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_peliculafavorita'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='favoritos',
            field=models.IntegerField(default=0),
        ),
    ]
