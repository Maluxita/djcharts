# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-09 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graficas', '0003_remove_examplesimple_float_8'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotasPeriodico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(default='', max_length=10)),
                ('r_2006', models.FloatField(default=0.0)),
                ('r_2007', models.FloatField(default=0.0)),
                ('r_2008', models.FloatField(default=0.0)),
                ('r_2009', models.FloatField(default=0.0)),
                ('r_2010', models.FloatField(default=0.0)),
                ('r_2011', models.FloatField(default=0.0)),
                ('r_2012', models.FloatField(default=0.0)),
                ('r_2013', models.FloatField(default=0.0)),
                ('r_2014', models.FloatField(default=0.0)),
                ('r_2015', models.FloatField(default=0.0)),
                ('r_2016', models.FloatField(default=0.0)),
            ],
        ),
    ]