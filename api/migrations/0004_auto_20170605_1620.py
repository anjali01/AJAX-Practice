# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-05 16:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170605_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='country_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='country_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='state',
            old_name='state_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='state',
            old_name='state_name',
            new_name='name',
        ),
    ]
