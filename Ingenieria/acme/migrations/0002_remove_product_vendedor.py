# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 03:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acme', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='vendedor',
        ),
    ]
