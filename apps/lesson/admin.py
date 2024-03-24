from django.contrib import admin
from apps.lesson.models import Grouplesson, Individuallesson

# Register your models here.


@admin.register(Grouplesson)
class GrouplessonAdmin(admin.ModelAdmin):
    list_display = ('category', 'creator')
    list_filter = ('category', 'creator')


@admin.register(Individuallesson)
class IndividuallessonAdmin(admin.ModelAdmin):
    list_display = ('category', 'creator')
    list_filter = ('category', 'creator')