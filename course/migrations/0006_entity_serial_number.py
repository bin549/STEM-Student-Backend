# Generated by Django 4.0.1 on 2022-02-08 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_entity_slug_genre_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='serial_number',
            field=models.IntegerField(default=1111, unique=True),
            preserve_default=False,
        ),
    ]
