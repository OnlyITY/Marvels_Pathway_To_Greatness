# Generated by Django 5.0.2 on 2024-04-20 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_comics_comicimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='comics',
            name='comicID',
            field=models.IntegerField(default=1),
        ),
    ]