# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-18 16:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aroundme', '0005_auto_20160918_0138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anniversary',
            name='member_sub',
        ),
        migrations.RemoveField(
            model_name='personalevent',
            name='member_sub',
        ),
        migrations.AlterField(
            model_name='anniversary',
            name='member_main',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='personalevent',
            name='member_main',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
