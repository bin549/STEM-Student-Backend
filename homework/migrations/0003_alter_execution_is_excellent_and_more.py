# Generated by Django 4.0.1 on 2022-02-10 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0002_rename_course_id_assignment_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='execution',
            name='is_excellent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='execution',
            name='is_finish',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='execution',
            name='score',
            field=models.IntegerField(null=True),
        ),
    ]
