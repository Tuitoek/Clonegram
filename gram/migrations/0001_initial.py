# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-11 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=20)),
                ('image_caption', models.CharField(max_length=20)),
                ('likes', models.CharField(max_length=1000)),
                ('comments', models.CharField(max_length=250)),
                ('image_path', models.ImageField(upload_to='images/')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
