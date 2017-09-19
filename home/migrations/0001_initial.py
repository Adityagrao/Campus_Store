# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 12:36
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
                ('name', models.CharField(blank=None, default=None, max_length=100, unique=True)),
                ('class_name', models.CharField(max_length=50)),
                ('bundle', models.CharField(max_length=20, unique=True)),
                ('particulars', models.CharField(max_length=50)),
                ('tax_code', models.CharField(default=None, max_length=50)),
                ('amount', models.FloatField()),
                ('tax_CGST', models.FloatField(default=0)),
                ('tax_SGST', models.FloatField(default=0)),
                ('total', models.FloatField()),
                ('grand_total', models.FloatField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_time', models.DateTimeField(auto_now_add=True)),
                ('total', models.FloatField()),
                ('processed', models.BooleanField(default=False)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Book')),
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
                ('alternate_email', models.CharField(max_length=50)),
                ('principal_name', models.CharField(max_length=100)),
                ('principal_email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=256)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('dob', models.DateField()),
                ('admission_number', models.CharField(max_length=50)),
                ('name_of_parent', models.CharField(max_length=50)),
                ('mobile_no', models.CharField(max_length=10)),
                ('email_id', models.CharField(max_length=75)),
                ('password', models.CharField(max_length=75)),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.School')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='school_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.School'),
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.User'),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Category'),
        ),
        migrations.AddField(
            model_name='book',
            name='school_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.School'),
        ),
    ]
