from django.urls import path

from apps.lesson.views import (
    LessonListGenericView,
    LessonDetailGenericView,
    LessonListForParentGenericView
)


urlpatterns = [
    path("", LessonListGenericView.as_view()),
    path("<int:subtask_id>/", LessonDetailGenericView.as_view()),
    path("mylessons/", LessonListForParentGenericView.as_view())
]
