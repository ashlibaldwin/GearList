# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_remove_item_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='user_profile',
            field=models.ForeignKey(to='polls.UserProfile', null=True),
        ),
    ]
