# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 02:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='produto',
            new_name='produto1',
        ),
    ]
