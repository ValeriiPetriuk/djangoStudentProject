from rest_framework import viewsets

from base.models import Schedule
from base.permisions.is_teacher import IsTeacher
from base.serializers.schedule_serializers import ScheduleModelSerializer
from rest_framework.permissions import AllowAny
from base.filters.schedule_filter import ScheduleFilter
from rest_framework.permissions import IsAuthenticated

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleModelSerializer
    filterset_class = ScheduleFilter

    def get_permissions(self):
        if self.action in ('create', 'update', 'delete'):
            permission_classes = [IsAuthenticated|IsTeacher]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]







