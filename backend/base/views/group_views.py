from rest_framework import viewsets
from base.models.groups_models import Group
from base.serializers.group_serializers import GroupSerializer

class GroupModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    
    