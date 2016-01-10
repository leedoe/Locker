# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Locker',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('floor', models.IntegerField()),
                ('section', models.CharField(max_length=45)),
                ('rNum', models.IntegerField()),
                ('cNum', models.IntegerField()),
                ('building', models.ForeignKey(to='LockerCustom.Building')),
                ('manager', models.ForeignKey(to='LockerCustom.Department')),
            ],
        ),
        migrations.CreateModel(
            name='LockerDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('row', models.IntegerField()),
                ('column', models.IntegerField()),
                ('check', models.IntegerField()),
                ('locker_number', models.ForeignKey(to='LockerCustom.Locker')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('user_id', models.CharField(max_length=10)),
                ('birth', models.CharField(max_length=12)),
                ('fee_check', models.IntegerField(choices=[('회비 미납', 0), ('회비 납부', 1)])),
                ('department', models.ForeignKey(to='LockerCustom.Department')),
            ],
        ),
        migrations.AddField(
            model_name='lockerdetail',
            name='user_id',
            field=models.ForeignKey(to='LockerCustom.UserInfo'),
        ),
    ]
