# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('buharisupport', '0003_auto_20171112_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='pooling_unit',
            field=models.CharField(default=datetime.datetime(2017, 11, 13, 1, 37, 41, 796775, tzinfo=utc), verbose_name='Members ward', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='members',
            name='ward',
            field=models.CharField(verbose_name='Members ward', max_length=70),
        ),
    ]
