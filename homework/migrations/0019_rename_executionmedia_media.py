# Generated by Django 4.0.1 on 2022-03-28 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0018_execution_content_text'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExecutionMedia',
            new_name='Media',
        ),
    ]