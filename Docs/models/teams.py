from django.db import models
from .users import Users


class Team(models.Model):
    name = models.CharField(max_length=40)
    member = models.ManyToManyField(Users, related_name='team')