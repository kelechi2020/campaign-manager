# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('buharisupport', '0002_auto_20171109_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoolingUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('poolingunit_name', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('ward_name', models.CharField(blank=True, max_length=200)),
                ('local_government', models.ForeignKey(to='buharisupport.LocalGovernment')),
            ],
        ),
        migrations.AddField(
            model_name='members',
            name='ward',
            field=models.CharField(verbose_name='Members ward', max_length=255, default=datetime.datetime(2017, 11, 12, 19, 17, 38, 669285, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='poolingunit',
            name='ward',
            field=models.ForeignKey(to='buharisupport.Ward'),
        ),
    ]
