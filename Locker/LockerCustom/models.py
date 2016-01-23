from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

"""
class UserInfo(models.Model):
    FEE = (
        (0, '회비 미납'),
        (1, '회비 납부'),
    )

    user_id = models.CharField(max_length=10)
    birth = models.CharField(max_length=12)
    fee_check = models.IntegerField(choices=FEE)
    department = models.ForeignKey(Department)

    def __str__(self):
        return self.user_id
"""


class UserInfo(AbstractUser):
    FEE = (
        (0, '회비 미납'),
        (1, '회비 납부'),
    )

    fee_check = models.IntegerField(choices=FEE, null=True)
    department = models.ForeignKey(Department, null=True)

    def __str__(self):
        return self.username


class Building(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class Locker(models.Model):
    building = models.ForeignKey(Building)
    floor = models.CharField(max_length=5)
    section = models.CharField(max_length=45)
    rNum = models.IntegerField()
    cNum = models.IntegerField()
    manager = models.ForeignKey(Department)

    def __str__(self):
        return str(self.building) + " " + str(self.floor) + "층 " + self.section


class LockerDetail(models.Model):
    CHECK = (
        (0, '예약 불가'),
        (1, '예약 가능')
    )

    locker_number = models.ForeignKey(Locker)
    row = models.IntegerField()
    column = models.IntegerField()
    check = models.IntegerField(choices=CHECK)
    user_id = models.ForeignKey(UserInfo, null=True, blank=True)

    def __str__(self):
        return str(self.locker_number) + " " + str(self.row) + ", " + str(self.column)
