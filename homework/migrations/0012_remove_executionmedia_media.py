# Generated by Django 4.0.1 on 2022-03-28 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0011_mediatype_executionmedia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='executionmedia',
            name='media',
        ),
    ]
