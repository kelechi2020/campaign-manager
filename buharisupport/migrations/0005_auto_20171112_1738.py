# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buharisupport', '0004_auto_20171112_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='pooling_unit',
            field=models.CharField(max_length=255, verbose_name='Pooling Unit'),
        ),
    ]
