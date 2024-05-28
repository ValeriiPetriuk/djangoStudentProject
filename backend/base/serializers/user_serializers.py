from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from base.models import User

from django.contrib.auth.hashers import make_password

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['email'] = user.email
        # ...

        return token


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('is_staff', 'is_active', 'date_joined',  'last_login', 'user_permissions',
                   'is_superuser')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


