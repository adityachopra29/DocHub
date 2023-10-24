from django.db import models
from .users import Users


class Document(models.Model):
    owner = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=40)
    delta = models.JSONField()
    text = models.TextField()
