# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LockerCustom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='fee_check',
            field=models.IntegerField(choices=[(0, '회비 미납'), (1, '회비 납부')], null=True),
        ),
    ]
