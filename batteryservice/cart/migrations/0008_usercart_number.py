# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-17 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_auto_20180318_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercart',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]