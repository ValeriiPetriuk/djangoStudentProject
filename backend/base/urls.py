from rest_framework import routers

from base.views.user_views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

