from rest_framework import serializers

from base.models import Schedule
from base.serializers.subject_serializers import SubjectModelSerializer
from base.serializers.group_serializers import GroupSerializer


class ScheduleModelSerializer(serializers.ModelSerializer):
    subject = SubjectModelSerializer(many=True)
    group = GroupSerializer()
    class Meta:
        model = Schedule
        fields = ("id", "day", "group", "subject",)