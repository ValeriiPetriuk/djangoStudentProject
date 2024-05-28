from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from base.models import User
from base.serializers import MyTokenObtainPairSerializer
from base.serializers.user_serializers import UserModelSerializer, RegisterSerializer
from rest_framework import generics


class ListViewUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class RegisterViewSet(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



