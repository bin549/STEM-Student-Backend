# Generated by Django 4.0.1 on 2022-03-28 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadmodel',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]