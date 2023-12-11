from django.urls import path, include
from rest_framework import routers
from Docs.views import *

router = routers.SimpleRouter()
router.register(r'users', UserViewSet, basename="users")
router.register(r'document', DocumentViewSet, basename="document")
router.register(r'user_access_permissions', UserPermissionViewSet, basename="user_access_permissions")


urlpatterns = [
    path("", include(router.urls)),
    path("auth/oauth/", RequestAccessAPI.as_view(), name='login'),
    path("home/", CallbackAPI.as_view(), name='home'),
    path("testing/", CheckView.as_view(), name='test'),
    path("logout/", LogoutUser.as_view(), name='logout_user'),
    path("clear/", ClearUserDB.as_view(), name='clear_db'),
    path("check_login/", CheckLogin.as_view(), name='check_login'),
]
