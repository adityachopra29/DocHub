from rest_framework import serializers
# from models.user import User
# from models.teams import Team
# from models.document import Document
from Docs.models.access_permissions import *
# from django.core.validators import MaxValueValidator, MinValueValidator


class UserPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccess
        fields = '__all__'


class TeamPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamAccess
        fields = '__all__'