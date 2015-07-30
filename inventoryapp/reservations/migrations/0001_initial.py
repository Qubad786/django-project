# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('price', models.DecimalField(default=0, decimal_places=3, max_digits=100)),
                ('ordered_units', models.IntegerField(default=0)),
                ('order_date', models.DateField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(to='products.Products', related_name='reservations')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='reservations')),
            ],
        ),
    ]
