# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-17 18:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20180317_2347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercart',
            old_name='cartname',
            new_name='cart_items',
        ),
    ]