from django.contrib import admin
from apps.lesson.models import Lesson

# Register your models here.


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('category', 'teacher', 'pupil')
    list_filter = ('category', 'teacher', 'pupil')
