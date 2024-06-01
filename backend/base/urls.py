from django.urls import path

from base.views.user_views import (
        MyTokenObtainPairView, ListViewUser,
        RegisterViewSet,  UserDetailView
    )


urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('register/', RegisterViewSet.as_view(), name='register'),
    path("users/",  ListViewUser.as_view(), name='users'),
    path("users/<str:username>/", UserDetailView.as_view()),
]


