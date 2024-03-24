from django.urls import path, include


app_name = 'router'


urlpatterns = [
    path('users/', include('apps.user.urls')),
    path('categories/', include('apps.category.urls')),
]