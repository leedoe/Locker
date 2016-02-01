# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LockerCustom', '0003_auto_20160112_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='lockerdetail',
            name='locker_detail_number',
            field=models.IntegerField(default=0),
        ),
    ]
