# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-17 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20180317_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercart',
            name='cart_items',
            field=models.ManyToManyField(blank=True, related_name='add', to='product.ProductDetail'),
        ),
    ]
