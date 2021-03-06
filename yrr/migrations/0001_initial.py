# Generated by Django 3.1.3 on 2020-11-26 19:33

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.CharField(auto_created=True, max_length=200, primary_key=True, serialize=False)),
                ('image', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='media/data/'), upload_to='')),
                ('name', models.CharField(max_length=200)),
                ('related_links', models.CharField(max_length=200, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.CharField(auto_created=True, max_length=200, primary_key=True, serialize=False)),
                ('phone_id', models.CharField(max_length=200)),
                ('image', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='media/log/'), upload_to='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
