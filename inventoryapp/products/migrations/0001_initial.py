# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('product_name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('units', models.IntegerField(default=0)),
                ('actual_unit_price', models.DecimalField(default=0, decimal_places=3, max_digits=100)),
                ('profit_factor', models.DecimalField(default=0, decimal_places=3, max_digits=100)),
                ('adding_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
