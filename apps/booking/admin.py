from django.contrib import admin
from apps.booking.models import Cabinet, Booking


@admin.register(Cabinet)
class CabinetAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('date','time_start', 'duration', 'cabinet')
    list_filter = ('date', 'duration', 'cabinet')
    search_fields = ('date',)
# Register your models here.
