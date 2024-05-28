from rest_framework.viewsets import ModelViewSet

from base.models import User
from base.serializers import UserModelSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer



