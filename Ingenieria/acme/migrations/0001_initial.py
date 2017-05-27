# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 02:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='acme/img/AvatarEstudiante.png', upload_to=b'')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=300)),
                ('stock', models.PositiveIntegerField()),
                ('avatar', models.ImageField(default='acme/img/pollo1.png', upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='VendedorAmbProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check', models.BooleanField(default=False)),
                ('avatar', models.ImageField(default='acme/img/AvatarVendedor4.png', upload_to=b'')),
                ('likes', models.PositiveIntegerField(default=0)),
                ('cash', models.BooleanField(default=True)),
                ('credit', models.BooleanField(default=False)),
                ('debit', models.BooleanField(default=False)),
                ('student', models.BooleanField(default=False)),
                ('dishes', models.ManyToManyField(blank=True, to='acme.Product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VendedorFijoProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('init_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('likes', models.PositiveIntegerField(default=0)),
                ('avatar', models.ImageField(default='acme/img/AvatarVendedor1.png', upload_to=b'')),
                ('cash', models.BooleanField(default=True)),
                ('credit', models.BooleanField(default=False)),
                ('debit', models.BooleanField(default=False)),
                ('student', models.BooleanField(default=False)),
                ('dishes', models.ManyToManyField(blank=True, to='acme.Product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
