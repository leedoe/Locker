from django.contrib import admin
from LockerCustom.models import *

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Building)
admin.site.register(Department)
admin.site.register(Locker)
admin.site.register(LockerDetail)