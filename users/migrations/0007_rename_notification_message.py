# Generated by Django 4.0.1 on 2022-02-16 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_recipient_id_notification_recipient_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notification',
            new_name='Message',
        ),
    ]
