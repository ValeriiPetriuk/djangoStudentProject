from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from base.models import User
from rest_framework.validators import UniqueValidator


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "surname", "email", "phone", "groups", "role")


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    password2 = serializers.CharField(max_length=128, min_length=8,  write_only=True, required=True)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "surname", "email", "phone", "password", "password2", "groups", "role")

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        validated_data.pop('password2', None)

        return User.objects.create_user(**validated_data)





