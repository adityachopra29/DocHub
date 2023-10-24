from rest_framework import serializers
from Docs.models.users import Users


class UserSerializer(serializers.ModelSerializer):
    # name = serializers.CharField()
    # email = serializers.EmailField()
    # date_of_joining = serializers.DateField()
    # tag = serializers.CharField(unique=True)
    class Meta:
        model = Users
        fields = ['__all__']