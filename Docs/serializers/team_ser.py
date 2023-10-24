from rest_framework import serializers
from Docs.models.teams import Team
# from models.user import User

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['__all__']