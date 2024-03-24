from django.contrib import admin
from apps.lesson.models import Lesson

# Register your models here.


# @admin.register(Grouplesson)
# class GrouplessonAdmin(admin.ModelAdmin):
#     list_display = ('category', 'teacher')
#     list_filter = ('category', 'teacher')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('category', 'teacher')
    list_filter = ('category', 'teacher')
