from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
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
    path("auth/login/", TokenObtainPairView.as_view()),
    path("auth/refresh-token/", TokenRefreshView.as_view()),
    path('users/<int:user_id>/pupils/', ListPupilsOfUserGenericView.as_view()),
    path('users/<int:user_id>/pupils/<int:pupil_id>/', PupilDetailGenericView.as_view(),),
]