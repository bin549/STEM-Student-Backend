# Generated by Django 4.0.1 on 2022-02-08 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_entity_serial_number2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entity',
            name='serial_number2',
        ),
    ]