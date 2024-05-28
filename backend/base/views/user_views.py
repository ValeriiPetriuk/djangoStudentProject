from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from base.models import User
from base.serializers import MyTokenObtainPairSerializer
from base.serializers.user_serializers import UserModelSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



