from django.contrib import admin
from apps.booking.models import Booking





@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('date','lesson', 'time_start', 'duration', 'cabinet')
    list_filter = ('date', 'duration', 'cabinet')
    search_fields = ('date',)
# Register your models here.
