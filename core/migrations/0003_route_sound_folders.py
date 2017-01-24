# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170124_0601'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='sound_folders',
            field=models.CharField(default='/farar', max_length=50),
            preserve_default=False,
        ),
    ]
