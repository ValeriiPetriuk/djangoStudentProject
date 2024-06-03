from django.contrib import admin

from base.models import User, Group, Subject

admin.site.register(User)
admin.site.register(Group)

admin.site.register(Subject)