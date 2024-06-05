from rest_framework import serializers

from base.models import Schedule
from base.serializers.subject_serializers import SubjectModelSerializer


class ScheduleModelSerializer(serializers.ModelSerializer):
    # subject = SubjectModelSerializer(many=True)
    class Meta:
        model = Schedule
        fields = ("day", "group", "subject",)