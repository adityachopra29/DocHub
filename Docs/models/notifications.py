from django.db import models
from .user import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Notification(models.Model):
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="to_user")
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.IntegerField(
        validators=[
            MaxValueValidator(4),
            MinValueValidator(1)
        ]
    )
    creation_time = models.TimeField()
