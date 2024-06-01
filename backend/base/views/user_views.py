from rest_framework_simplejwt.views import TokenObtainPairView
from base.models import User
from base.serializers import MyTokenObtainPairSerializer
from base.serializers.user_serializers import UserModelSerializer, RegisterSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


class ListViewUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['groups']


class RegisterViewSet(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    lookup_field = 'username'


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer