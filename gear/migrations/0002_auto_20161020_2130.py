# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-21 02:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(max_length=250, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='list',
            name='title',
            field=models.CharField(max_length=250, verbose_name=''),
        ),
    ]