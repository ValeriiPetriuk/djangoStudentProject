from rest_framework import routers

from django.urls import path, include

from base.views.user_views import MyTokenObtainPairView, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
]


