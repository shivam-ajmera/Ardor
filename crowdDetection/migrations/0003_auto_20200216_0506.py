# Generated by Django 2.2.7 on 2020-02-16 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdDetection', '0002_musicsession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicsession',
            name='artist',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='movie',
            field=models.TextField(unique=True),
        ),
    ]
