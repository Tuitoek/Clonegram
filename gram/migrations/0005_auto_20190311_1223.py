# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-11 09:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0004_auto_20190311_1120'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]