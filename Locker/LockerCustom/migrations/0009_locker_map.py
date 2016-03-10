# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LockerCustom', '0008_auto_20160218_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='locker',
            name='map',
            field=models.FileField(upload_to='map/', null=True),
        ),
    ]
