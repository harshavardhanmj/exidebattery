# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-17 08:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercart',
            name='name',
        ),
    ]