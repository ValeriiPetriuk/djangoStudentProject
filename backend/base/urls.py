from rest_framework import routers

from django.urls import path, include

from base.views.user_views import MyTokenObtainPairView, ListViewUser, RegisterViewSet
#
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('register/', RegisterViewSet.as_view(), name='register'),
    path("users/",  ListViewUser.as_view(), name='users'),
]


