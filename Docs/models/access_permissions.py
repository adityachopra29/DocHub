from django.db import models
from .users import Users
from .teams import Team
from .document import Document
from django.core.validators import MaxValueValidator, MinValueValidator


class UserAccess(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    for_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    permission_level = models.IntegerField(
        validators=[
            MaxValueValidator(4),
            MinValueValidator(1)
        ]
    )

class TeamAccess(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    for_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    permission_level = models.IntegerField(
        validators=[
            MaxValueValidator(4),
            MinValueValidator(1)
        ]
    )
