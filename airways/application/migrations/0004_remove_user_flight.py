# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-18 12:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20180718_1009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='flight',
        ),
    ]