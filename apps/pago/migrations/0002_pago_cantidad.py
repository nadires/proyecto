# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-15 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pago', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='cantidad',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]