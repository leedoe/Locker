# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LockerCustom', '0007_excelpath'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excelpath',
            name='excelpath',
            field=models.FileField(upload_to='excel/'),
        ),
    ]
