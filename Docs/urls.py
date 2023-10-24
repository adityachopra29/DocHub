from django.urls import path
from Docs.views.oauth.login import *
from Docs.views.testing import *


urlpatterns = [
    path("", RequestAccessAPI.as_view(), name='login'),
    path("home/", CallbackAPI.as_view(), name='home'),
    path("testing/", CheckView.as_view(), name='test'),
    path("logout/", LogoutUser.as_view(), name='logout_user'),
    path("clear/", ClearDB.as_view(), name='clear_db')
]
