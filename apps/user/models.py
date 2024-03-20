from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)

from django.utils.translation import gettext_lazy

from apps.user.manager import UserManager
from django.core.exceptions import ValidationError


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=100,
        unique=True,
        verbose_name=gettext_lazy("Email address")
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name=gettext_lazy("First name")
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name=gettext_lazy("Last name")
    )
    username = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )
    phone = models.CharField(max_length=25)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Pupil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(
        max_length=50,
        verbose_name=gettext_lazy("First name")
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name=gettext_lazy("Last name")
    )
    date_of_birth = models.DateField()
    description = models.TextField(
        max_length=1500,
        verbose_name="problems",
        default="Here you can add your description..."
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
