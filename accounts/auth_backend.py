from django.contrib.auth.backends import BaseBackend
from .models import Center

class CenterBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            center = Center.objects.get(username=username)
            if center.password == password:  # ⚠ Consider hashing later
                return center
        except Center.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Center.objects.get(pk=user_id)
        except Center.DoesNotExist:
            return None
