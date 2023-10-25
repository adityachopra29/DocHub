from django.contrib import admin
from .models.user import User
from .models.teams import Team
from .models.document import Document
# from .models.notifications import Notification
from .models.access_permissions import UserAccess, TeamAccess

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'date_of_joining', 'tag']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

# @admin.register(Notification)
# class NotificationAdmin(admin.ModelAdmin):
#     list_display = ['id', 'type', 'creation_time']


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'owner', 'text']


@admin.register(UserAccess)
class UserAccessAdmin(admin.ModelAdmin):
    list_display = ['id', 'document', 'for_user', 'permission_level']


@admin.register(TeamAccess)
class TeamAccessAdmin(admin.ModelAdmin):
    list_display = ['id', 'document', 'for_team', 'permission_level']
