# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20160712_1926'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={},
        ),
        migrations.AlterModelOptions(
            name='list',
            options={},
        ),
        migrations.RemoveField(
            model_name='item',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='item',
            name='priority',
        ),
    ]
