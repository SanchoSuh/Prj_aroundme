# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-27 15:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('aroundme', '0007_auto_20160921_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalevent',
            name='datetime_finish',
        ),
        migrations.RemoveField(
            model_name='personalevent',
            name='datetime_start',
        ),
        migrations.AddField(
            model_name='personalevent',
            name='date_finish',
            field=models.DateField(default=datetime.datetime(2016, 9, 27, 15, 8, 17, 919061, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalevent',
            name='date_start',
            field=models.DateField(default=datetime.datetime(2016, 9, 27, 15, 8, 25, 54905, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
