# Generated by Django 4.0.1 on 2022-01-27 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='course_id',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='execution',
            old_name='homework_id',
            new_name='homework',
        ),
        migrations.RenameField(
            model_name='execution',
            old_name='user_id',
            new_name='user',
        ),
    ]
