# Generated by Django 4.0.1 on 2022-03-28 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0020_alter_entity_options_alter_genre_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['comment_time']},
        ),
    ]