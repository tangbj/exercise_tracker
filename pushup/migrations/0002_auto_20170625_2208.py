# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 14:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pushup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
