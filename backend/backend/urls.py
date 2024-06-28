from django.contrib import admin
from django.urls import path, include

# from base.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include("base.urls")),
    # path('api/', include(router.urls))
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
