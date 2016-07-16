# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20160715_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Item Name'),
        ),
        migrations.AlterField(
            model_name='list',
            name='title',
            field=models.CharField(unique=True, max_length=250, verbose_name='List Name'),
        ),
    ]
