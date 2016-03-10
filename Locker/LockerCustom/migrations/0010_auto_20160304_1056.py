# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LockerCustom', '0009_locker_map'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locker',
            name='map',
            field=models.ImageField(upload_to='map/', null=True),
        ),
    ]
