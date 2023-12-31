from rest_framework import viewsets
from Docs.models.user import User
from Docs.serializers.user import UserSerializer
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    ordering_fields = ['username', 'email', 'enrollment_no']
    ordering = ['name']
    permission_classes=[IsAuthenticated]

    