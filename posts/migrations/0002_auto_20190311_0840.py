# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-11 08:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 11, 8, 40, 45, 593674, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
