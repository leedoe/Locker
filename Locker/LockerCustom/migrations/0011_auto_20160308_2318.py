# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LockerCustom', '0010_auto_20160304_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='locker',
            name='start_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='locker',
            name='map',
            field=models.ImageField(upload_to='media/', null=True),
        ),
    ]
