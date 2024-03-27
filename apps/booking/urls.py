from django.urls import path
from apps.booking.views import (
    BookingListGenericView,
    BookingListwritableGenericView,
    BookingDetailGenericView,
    BookingwriteGenericView,
    BookingListForParentGenericView
)


urlpatterns = [
    path("", BookingListGenericView.as_view()),
    path("<int:booking_id>/", BookingDetailGenericView.as_view()),
    path("mybookings/", BookingListForParentGenericView.as_view()),
    path("writable/", BookingListwritableGenericView.as_view()),
    path("writable/<int:booking_id>/", BookingwriteGenericView.as_view()),

]