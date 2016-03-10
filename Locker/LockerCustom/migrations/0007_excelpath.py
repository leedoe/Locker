# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LockerCustom', '0006_auto_20160205_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='excelPath',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('excelpath', models.FilePathField(path='/excel')),
                ('department', models.OneToOneField(to='LockerCustom.Department')),
            ],
        ),
    ]
