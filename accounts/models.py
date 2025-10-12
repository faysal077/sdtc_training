# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from centers.models import Center

class AccountManager(BaseUserManager):
    def create_user(self, username, password=None, center=None, **extra_fields):
        if not username:
            raise ValueError("The Username must be set")
        user = self.model(username=username, center=center, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    center = models.ForeignKey(Center, on_delete=models.CASCADE, null=True, blank=True)
    is_staff = models.BooleanField(default=False)  # required for Django admin
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "Account"

    def __str__(self):
        return f"{self.username} ({self.center.District if self.center else 'No Center'})"
