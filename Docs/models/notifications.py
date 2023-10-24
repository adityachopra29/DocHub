# from django.db import models
# from .user import User
# from django.core.validators import MaxValueValidator, MinValueValidator

# class Notification(models.Model):
#     to_user = models.ManyToManyField(User)
#     from_user = models.ManyToManyField(User)
#     type = models.IntegerField(
#         validators=[
#             MaxValueValidator(4),
#             MinValueValidator(1)
#         ]
#     )
#     creation_time = models.TimeField()
