from rest_framework import serializers

from base.models import User


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('is_staff', 'is_active', 'date_joined', 'password', 'last_login', 'user_permissions',
                   'is_superuser')
