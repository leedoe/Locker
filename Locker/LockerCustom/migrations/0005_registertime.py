# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LockerCustom', '0004_lockerdetail_locker_detail_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='registerTime',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('department', models.ForeignKey(to='LockerCustom.Department', unique=True)),
            ],
        ),
    ]
