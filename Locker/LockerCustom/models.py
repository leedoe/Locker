from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    FEE = (
        ('회비 미납', 0),
        ('회비 납부', 1),
    )

    user_id = models.CharField(max_length=10)
    birth = models.CharField(max_length=12)
    fee_check = models.IntegerField(choices=FEE)
    department = models.ForeignKey(Department)


class Building(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class Locker(models.Model):
    building = models.ForeignKey(Building)
    floor = models.IntegerField()
    section = models.CharField(max_length=45)
    rNum = models.IntegerField()
    cNum = models.IntegerField()
    manager = models.ForeignKey(Department)

    def __str__(self):
        return self.id


class LockerDetail(models.Model):
    CHECK = (
        ('예약 불가', 0),
        ('예약 가능', 1)
    )

    locker_number = models.ForeignKey(Locker)
    row = models.IntegerField()
    column = models.IntegerField()
    check = models.IntegerField()
    user_id = models.ForeignKey(UserInfo)

    def __str__(self):
        return self.locker_number
