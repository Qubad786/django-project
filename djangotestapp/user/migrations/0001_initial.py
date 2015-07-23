# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='email address')),
                ('username', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Anchors',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('link', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='UrlData',
            fields=[
                ('url', models.CharField(serialize=False, max_length=250, primary_key=True)),
                ('tags_count', models.IntegerField(default=0)),
                ('meta_tags_count', models.IntegerField(default=0)),
                ('size', models.IntegerField(default=0)),
                ('date_time', models.DateTimeField(default=None)),
            ],
        ),
        migrations.AddField(
            model_name='anchors',
            name='url',
            field=models.ForeignKey(to='user.UrlData', related_name='anchors'),
        ),
    ]
