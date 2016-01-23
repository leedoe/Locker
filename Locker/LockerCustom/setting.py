from django.conf import settings
from django.contrib.auth.models import User, check_password


class SettingBackend(object):
    def authenticate(self, username = None, password = None):
        login_vaild = (settings.ADMIN_LOGIN == username)
        pwd_vaild = (check_password(password, settings.ADMIN_PASSWORD))
        if login_vaild and pwd_vaild:
            try:
                user = User.objects.get(username = username)
            except User.DoesNotExist:
                return None
            return user
        return None

    def get_user(self, user_id):
            try:
                return User.objects.get(pk = user_id)
            except User.DoesNotExist:
                return None

    def has_perm(self, user_obj, perm, obj=None):
        if user_obj.username == settings.ADMIN_LOGIN:
            return True
        else:
            return False