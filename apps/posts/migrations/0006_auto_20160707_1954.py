# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20160707_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
