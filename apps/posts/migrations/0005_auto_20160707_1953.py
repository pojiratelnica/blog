# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20160707_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='display',
            field=models.BooleanField(default=True),
        ),
    ]