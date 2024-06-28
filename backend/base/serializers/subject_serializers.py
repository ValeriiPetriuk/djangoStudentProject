from rest_framework import serializers

from base.models import Subject
from base.serializers import UserModelSerializer


class SubjectModelSerializer(serializers.ModelSerializer):
    teacher = UserModelSerializer()
    class Meta:
        model = Subject
        fields = ("name", "teacher")