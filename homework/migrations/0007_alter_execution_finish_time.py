# Generated by Django 4.0.1 on 2022-02-19 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0006_alter_execution_finish_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='execution',
            name='finish_time',
            field=models.DateTimeField(null=True),
        ),
    ]