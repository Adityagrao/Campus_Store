# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-22 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170822_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='School_name',
            field=models.CharField(max_length=50),
        ),
    ]