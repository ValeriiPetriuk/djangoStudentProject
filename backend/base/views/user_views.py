from rest_framework_simplejwt.views import TokenObtainPairView
from base.filters.user_filter import UserFilter
from base.models import User
from base.serializers import MyTokenObtainPairSerializer
from base.serializers.user_serializers import UserModelSerializer, RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class ListViewUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    filterset_class = UserFilter


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()


class UpdateUserView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserModelSerializer

    def get_object(self):
        return self.request.user


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    lookup_field = 'username'


class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserModelSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer