from django_filters import rest_framework as filters

from base.models import Group, User


class UserFilter(filters.FilterSet):
    group_choices = [(group.name, group.name) for group in Group.objects.all()]
    groups = filters.ChoiceFilter(field_name='groups__name', choices=group_choices)


    class Meta:
        model = User
        fields = ['groups']
