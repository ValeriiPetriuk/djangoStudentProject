from django.urls import path

from base.views.user_views import (
        MyTokenObtainPairView, ListViewUser,
        RegisterView,  UserDetailView,
        UpdateUserView, CurrentUserView
    )


urlpatterns = [

    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path("users/",  ListViewUser.as_view(), name='users'),
    path("users/me/", CurrentUserView.as_view(), name='current-user'),
    path("users/update/", UpdateUserView.as_view()),
    path("users/<str:username>/", UserDetailView.as_view()),
]


