# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='user_profile',
            field=models.ForeignKey(to='polls.UserProfile'),
        ),
        migrations.AddField(
            model_name='list',
            name='user_profile',
            field=models.ForeignKey(to='polls.UserProfile'),
        ),
    ]
