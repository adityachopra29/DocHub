from rest_framework import serializers
# from models.user import User
# from models.teams import Team
# from models.document import Document
from Docs.models.access_permissions import *
# from django.core.validators import MaxValueValidator, MinValueValidator


class UserPermissionsSerializer(serializers.ModelSerializer):
    # document = serializers.ForeignKey(Document, on_delete=serializers.CASCADE)
    # for_user = serializers.ForeignKey(User, on_delete=serializers.CASCADE)
    # permission_level = serializers.IntegerField(
    #     validators=[
    #         MaxValueValidator(4),
    #         MinValueValidator(1)
    #     ]
    # )
    class Meta:
        model = UserAccess
        fields = ['__all__']


class TeamPermissionsSerializer(serializers.ModelSerializer):
    # document = serializers.ForeignKey(Document, on_delete=serializers.CASCADE)
    # for_team = serializers.ForeignKey(Team, on_delete=serializers.CASCADE)
    # permission_level = serializers.IntegerField(
    #     validators=[
    #         MaxValueValidator(4),
    #         MinValueValidator(1)
    #     ]
    # )
    class Meta:
        model = TeamAccess
        fields = ['__all__']