# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buharisupport', '0006_auto_20171112_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='landmark_identity',
            field=models.CharField(null=True, verbose_name='Landmark', blank=True, max_length=400),
        ),
    ]
