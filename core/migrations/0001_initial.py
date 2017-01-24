# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incoming',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('date_start', models.DateTimeField(auto_now_add=True)),
                ('date_end', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=10)),
                ('code', models.PositiveSmallIntegerField(unique=True)),
                ('start_url', models.CharField(max_length=255)),
                ('normal_url', models.CharField(max_length=255)),
                ('end_url', models.CharField(max_length=255)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modify', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='incoming',
            name='route',
            field=models.ForeignKey(to='core.Route'),
        ),
    ]
