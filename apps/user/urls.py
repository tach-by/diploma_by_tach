from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView
)
from apps.jwt_config.views import (
    CustomTokenObtainPairView
)


from apps.user.views import (
    UserRegistrationGenericView,
    ListUsersGenericView,
    UserDetailGenericView,
    PupilDetailGenericView,
    ListPupilsOfUserGenericView
)


urlpatterns = [
    path("", ListUsersGenericView.as_view()),
    path("<int:user_id>/", UserDetailGenericView.as_view()),
    path("register/", UserRegistrationGenericView.as_view()),
    path("auth/login/", CustomTokenObtainPairView.as_view()),
    path("auth/refresh-token/", TokenRefreshView.as_view()),
    path('pupils/', ListPupilsOfUserGenericView.as_view()),
    path('pupils/<int:pupil_id>/', PupilDetailGenericView.as_view(),),
]