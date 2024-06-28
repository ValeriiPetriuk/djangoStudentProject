from django_filters import rest_framework as filters

from base.models import Schedule



class ScheduleFilter(filters.FilterSet):
    group = filters.CharFilter(field_name='group__name')
    class Meta:
        model = Schedule
        fields = ['day', 'group']
