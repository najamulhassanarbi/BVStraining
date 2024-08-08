from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from users.managers import CustomUserManager


class Role(models.TextChoices):
    """
    Enum for user roles.
    """
    GENERAL_USER = 'GENERAL_USER', _('General User')
    ADMIN = 'ADMIN', _('Admin')


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model with email, first name, last name, role, and timestamps.
    """
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(_("first name"), max_length=30)
    last_name = models.CharField(_("last name"), max_length=30)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(
        _("role"),
        max_length=20,
        choices=Role.choices,
        default=Role.GENERAL_USER
    )
    avatar = models.ImageField(default="default.jpg", upload_to="profile_images/")
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    bio = models.TextField(default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

    def __str__(self):
        """
        Return the string representation of the user, which is the email address.

        :return: User's email address
        :rtype: str
        """
        return self.email
