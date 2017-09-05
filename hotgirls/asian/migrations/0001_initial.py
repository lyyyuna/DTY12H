# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 03:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='error', max_length=50)),
                ('cover', models.URLField(default='error')),
                ('content', models.TextField(default='error')),
            ],
        ),
    ]
