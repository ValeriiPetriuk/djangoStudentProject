from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from base.views.user_views import (
        MyTokenObtainPairView, ListViewUser,
        RegisterView,  UserDetailView,
        UpdateUserView, CurrentUserView,
    )
from base.views.subject_views import SubjectViewSet
from base.views.schedule_views import ScheduleViewSet
from base.views.group_views import GroupModelViewSet

router = DefaultRouter()
router.register(r'subject', SubjectViewSet)

router.register(r'schedule', ScheduleViewSet)
router.register(r'groups', GroupModelViewSet)

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path("users/",  ListViewUser.as_view(), name='users'),
    path("users/me/", CurrentUserView.as_view(), name='current-user'),
    path("users/update/", UpdateUserView.as_view()),
    path("users/<str:username>/", UserDetailView.as_view()),

    path('', include(router.urls)),
]


