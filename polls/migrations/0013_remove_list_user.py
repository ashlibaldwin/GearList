# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_list_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='user',
        ),
    ]
