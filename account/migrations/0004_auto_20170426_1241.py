# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-26 04:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20170422_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='user/default/Path.png', upload_to='users/%Y/%m/%d'),
        ),
    ]