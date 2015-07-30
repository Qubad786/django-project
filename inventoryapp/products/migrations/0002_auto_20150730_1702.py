# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='adding_date',
            new_name='added_on',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='product_name',
            new_name='kind',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='type',
            new_name='name',
        ),
    ]
