from django.contrib import admin
from apps.lesson.models import Category, Grouplesson, Individuallesson

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'price')
    list_filter = ('name', 'duration', 'price')
    search_fields = ('name',)


@admin.register(Grouplesson)
class GrouplessonAdmin(admin.ModelAdmin):
    list_display = ('category', 'creator')
    list_filter = ('category', 'creator')


@admin.register(Individuallesson)
class IndividuallessonAdmin(admin.ModelAdmin):
    list_display = ('category', 'creator')
    list_filter = ('category', 'creator')