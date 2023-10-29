from django.urls import path, include
from rest_framework import routers
from Docs.views import *

router = routers.SimpleRouter()
# router.register(r'users', UserViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("auth/oauth", RequestAccessAPI.as_view(), name='login'),
    path("home/", CallbackAPI.as_view(), name='home'),
    path("testing/", CheckView.as_view(), name='test'),
    path("logout/", LogoutUser.as_view(), name='logout_user'),
    path("clear/", ClearDB.as_view(), name='clear_db'),
    path("users/", UserViewSet.as_view({
        'get':'list'
    })),
    path("users/<int:pk>", UserViewSet.as_view({
        'get':'retrieve'
    }))
]
