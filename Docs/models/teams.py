from django.db import models
from .user import User


class Team(models.Model):
    name = models.CharField(max_length=40)
    member = models.ManyToManyField(User, related_name='team')