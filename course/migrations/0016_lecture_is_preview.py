# Generated by Django 4.0.1 on 2022-02-18 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0015_lecture_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='is_preview',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
