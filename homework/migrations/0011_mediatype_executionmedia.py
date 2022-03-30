# Generated by Django 4.0.1 on 2022-03-28 10:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0010_delete_executionmedia_delete_mediatype'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExecutionMedia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('media', models.ImageField(blank=True, null=True, upload_to='')),
                ('execution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homework.execution')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homework.mediatype')),
            ],
        ),
    ]