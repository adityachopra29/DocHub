from rest_framework import serializers
from Docs.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'enrollment_no', 'email', 'tag', 'phone_no', 'date_of_joining']