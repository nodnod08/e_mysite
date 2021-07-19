from django.contrib.auth.backends import BaseBackend
from account.models import MyUser

class UserBackend(BaseBackend):
    def authenticate(request, email=None, password=None):
        try:
            user = MyUser.objects.get(email=email)
            password_valid = user.check_password(password)
            if password_valid:
                return user
            else:
                return None
        except MyUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return MyUser.objects.get(pk=user_id)
        except MyUser.DoesNotExist:
            return None