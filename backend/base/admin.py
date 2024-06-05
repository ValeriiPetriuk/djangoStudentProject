from django.contrib import admin

from base.models import User, Group, Subject, Replacement, Schedule

admin.site.register(User)
admin.site.register(Group)

admin.site.register(Subject)
admin.site.register(Schedule)
admin.site.register(Replacement)
