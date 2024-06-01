from rest_framework_simplejwt.views import TokenObtainPairView
from base.models import User
from base.serializers import MyTokenObtainPairSerializer
from base.serializers.user_serializers import UserModelSerializer, RegisterSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response



class ListViewUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['groups']
    permission_classes = [IsAuthenticated]


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()


class UpdateUserView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserModelSerializer

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        user = self.get_object()

        data = request.data

        user.username = data['username']
        user.email = data['email']

        user.save()
        serializer = self.get_serializer(user)
        return Response(serializer.data)


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