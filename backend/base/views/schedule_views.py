from rest_framework import viewsets
from rest_framework.response import Response
from base.models import Schedule
from base.permisions.is_teacher import IsTeacher
from base.serializers.schedule_serializers import ScheduleModelSerializer
from rest_framework.permissions import AllowAny


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleModelSerializer

    def get_permissions(self):
        if self.action in ('create', 'update'):
            permission_classes = [IsTeacher]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]







