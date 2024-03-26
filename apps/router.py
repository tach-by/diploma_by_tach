from django.urls import path, include


app_name = 'router'


urlpatterns = [
    path('users/', include('apps.user.urls')),
    path('categories/', include('apps.category.urls')),
    path('lessons/', include('apps.lesson.urls')),
    path('bookings/', include('apps.booking.urls')),
    path('cabinets/', include('apps.cabinet.urls'))

]