# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 19:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acme', '0008_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='client',
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='seller',
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]