from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Users(AbstractUser):
    username = models.CharField(
        max_length=50, blank=True, null=True, unique=True)
    enrollment_no = models.BigIntegerField(null=False, default=10)
    email = models.EmailField(_('email address'), unique=True)
    date_of_joining = models.DateField()
    phone_no = models.BigIntegerField(null=False)
    tag = models.CharField(unique=True)
