from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import os


# Create your models here.
# 학부 정보
class Department(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


# 유저 정보
class UserInfo(AbstractUser):
    FEE = (
        (0, '회비 미납'),
        (1, '회비 납부'),
    )

    fee_check = models.IntegerField(choices=FEE, null=True)
    department = models.ForeignKey(Department, null=True)

    def __str__(self):
        return self.username


# 건물 정보
class Building(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


# 사물함 정보
class Locker(models.Model):
    building = models.ForeignKey(Building)
    floor = models.CharField(max_length=5)
    section = models.CharField(max_length=45)
    rNum = models.IntegerField()
    cNum = models.IntegerField()
    manager = models.ForeignKey(Department)
    map = models.ImageField(upload_to='media/', null=True)
    start_number = models.IntegerField()

    def __str__(self):
        return str(self.building) + " " + str(self.floor) + "층 " + self.section


# 사물함 세부 정보
class LockerDetail(models.Model):
    CHECK = (
        (0, '예약 불가'),
        (1, '예약 가능')
    )

    locker_number = models.ForeignKey(Locker)
    locker_detail_number = models.IntegerField(default=0)
    row = models.IntegerField()
    column = models.IntegerField()
    check = models.IntegerField(choices=CHECK)
    user_id = models.ForeignKey(UserInfo, null=True, blank=True)

    def __str__(self):
        return str(self.locker_number) + " " + str(self.locker_detail_number)

    def get_check(self):
        return self.check

    def get_id(self):
        return self.id


class RegisterTime(models.Model):
    department = models.OneToOneField(Department)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.department.__str__()


class ExcelPath(models.Model):
    department = models.OneToOneField(Department)
    excelpath = models.FileField(upload_to='excel/')

    def __str__(self):
        return self.department.__str__()
