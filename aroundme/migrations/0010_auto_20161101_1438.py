# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-11-01 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aroundme', '0009_auto_20161027_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(default='default/default_member_icon.png', upload_to='%Y/%m/%d/'),
        ),
    ]
