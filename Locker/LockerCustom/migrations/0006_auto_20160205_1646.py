# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LockerCustom', '0005_registertime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registertime',
            name='department',
            field=models.OneToOneField(to='LockerCustom.Department'),
        ),
    ]
