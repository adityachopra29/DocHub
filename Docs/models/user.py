from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = models.CharField(
        max_length=50)
    enrollment_no = models.CharField(max_length=8)
    email = models.EmailField(_('email address'), unique=True)
    date_of_joining = models.DateField()
    phone_no = models.CharField(max_length=10, null=True, blank=True)
    tag = models.CharField(unique=True)
    # profile_picture = models.ImageField(upload_to="")

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username', 'enrollment_no']

    def __str__(self) :
        return f"Username: {self.username}, enrollment no: {self.enrollment_no}"
