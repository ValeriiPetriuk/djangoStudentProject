__all__ = (
    "UserModelSerializer",
    "MyTokenObtainPairSerializer",
    "RegisterSerializer",
    "ScheduleModelSerializer"
)

from base.serializers.user_serializers import (UserModelSerializer,
                                               MyTokenObtainPairSerializer,
                                               RegisterSerializer)
from base.serializers.schedule_serializers import ScheduleModelSerializer