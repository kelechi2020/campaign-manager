# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(verbose_name='First Name', max_length=40)),
                ('last_name', models.CharField(verbose_name='Surname', max_length=40)),
                ('mothers_maiden_name', models.CharField(blank=True, max_length=40, verbose_name='Mothers Maiden Name')),
                ('address', models.CharField(verbose_name='Address', max_length=100)),
                ('state', models.CharField(verbose_name='State', max_length=100, choices=[('ABIA', 'ABIA'), ('ADAMAWA', 'ADAMAWA'), ('AKWAIBOM', 'AKWAIBOM'), ('ANAMBRA', 'ANAMBRA'), ('BAUCHI', 'BAUCHI'), ('BAYELSA', 'BAYELSA'), ('BENUE', 'BENUE'), ('BORNO', 'BORNO'), ('CROSSRIVERS', 'CROSSRIVERS'), ('DELTA', 'DELTA'), ('EBONYI', 'EBONYI'), ('EDO', 'EDO'), ('EKITI', 'EKITI'), ('ENUGU', 'ENUGU'), ('GOMBE', 'GOMBE'), ('IMO', 'IMO'), ('JIGAWA', 'JIGAWA'), ('KADUNA', 'KADUNA'), ('KANO', 'KANO'), ('KATSINA', 'KATSINA'), ('KEBBI', 'KEBBI'), ('KOGI', 'KOGI'), ('KWARA', 'KWARA'), ('LAGOS', 'LAGOS'), ('NASARAWA', 'NASARAWA'), ('NIGER', 'NIGER'), ('OGUN', 'OGUN'), ('ONDO', 'ONDO'), ('OSUN', 'OSUN'), ('OYO', 'OYO'), ('PLATEAU', 'PLATEAU'), ('RIVERS', 'RIVERS'), ('SOKOTO', 'SOKOTO'), ('TARABA', 'TARABA'), ('YOBE', 'YOBE'), ('ZAMFARA', 'ZAMFARA')])),
                ('local_government', models.CharField(verbose_name='Local Government', max_length=70)),
                ('sex', models.CharField(verbose_name='Sex', max_length=10, choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')])),
                ('district', models.CharField(blank=True, max_length=600, verbose_name='District')),
                ('landmark_identity', models.CharField(blank=True, max_length=400, verbose_name='Landmark')),
                ('phone_number', models.CharField(verbose_name='Phone Number', max_length=30)),
                ('email', models.EmailField(verbose_name='E-mail', max_length=100)),
                ('communication_means1', models.NullBooleanField(verbose_name='Ist Means Of Communication')),
                ('communication_means2', models.NullBooleanField(verbose_name='Second Means Of Communication')),
            ],
        ),
        migrations.CreateModel(
            name='LocalGovernment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='localgovernment',
            name='country',
            field=models.ForeignKey(to='buharisupport.State'),
        ),
    ]
