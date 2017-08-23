# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-22 15:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=50)),
                ('bundle', models.CharField(max_length=20)),
                ('particulars', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('tax_CGST', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('tax_SGST', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('phone_no', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
                ('a_email', models.CharField(max_length=50)),
                ('principal_name', models.CharField(max_length=100)),
                ('principal_email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=256)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='School_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.School'),
        ),
    ]