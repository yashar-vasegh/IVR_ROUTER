# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_route_sound_folders'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='is_enable',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
