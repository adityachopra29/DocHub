from django.db import models
from .user import User


class Document(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=40)
    delta = models.JSONField(default={})
    text = models.TextField()

    # def __str__(self) :
    #     return f"Document name: {self.name}, owner:  {self.owner}"
