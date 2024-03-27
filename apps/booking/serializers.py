from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.booking.models import Booking
from apps.cabinet.models import Cabinet
from apps.user.models import Pupil
from apps.booking.error_messages import (
    BOOKING_DURATION_ERROR_MESSAGE,
    BOOKING_TIME_ERROR_MESSAGE
)
from apps.lesson.models import Lesson
from datetime import timedelta
from apps.booking.utils import calculate_time_end


def validate_fields(attrs):
    cabinet = attrs.get('cabinet')
    date = attrs.get('date')
    time_start = attrs.get('time_start')
    time_end = attrs.get('time_end')
    duration = attrs.get('duration')

    if duration:

        try:
            timedelta(hours=int(duration.split(':')[0]), minutes=int(duration.split(':')[1]),
                      seconds=int(duration.split(':')[2]))
        except (ValueError, IndexError):
            raise serializers.ValidationError(BOOKING_DURATION_ERROR_MESSAGE)


    existing_bookings = Booking.objects.filter(cabinet=cabinet, date=date)
    for booking in existing_bookings:
        if (booking.time_start <= time_start < booking.time_end) or (
                booking.time_start < time_end <= booking.time_end):
            raise serializers.ValidationError(BOOKING_TIME_ERROR_MESSAGE)

    return attrs

class BookingSerializer(serializers.ModelSerializer):
    creator = serializers.StringRelatedField()
    lesson = serializers.SlugRelatedField(
        slug_field='get_full_name',
        queryset=Lesson.objects.all()
    )
    cabinet = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Cabinet.objects.all(),
    )


    class Meta:
        model = Booking
        fields = [
            'creator',
            'date',
            'cabinet',
            'lesson',
            'time_start',
            'duration',
            'time_end',
            'repeat',
            'writable'
        ]

    def to_internal_value(self, data):

        duration = data.get('duration')
        time_start = data.get('time_start')
        time_end = data.get('time_end')
        date = data.get('date')

        if not duration:
            lesson_id = data['lesson']
            lesson = Lesson.objects.get(id=lesson_id)
            duration = lesson.category.duration
            data['duration'] = duration
        if not time_end:
            time_end = calculate_time_end(date, time_start, duration)
            data['time_end'] = time_end
        return super().to_internal_value(data)

    def validate(self, attrs):
        return validate_fields(attrs=attrs)


class BookingwritableSerializer(serializers.ModelSerializer):
    creator = serializers.StringRelatedField(read_only=True)
    cabinet = serializers.StringRelatedField(read_only=True)
    lesson = serializers.SlugRelatedField(
        slug_field='get_full_name',
        queryset=Lesson.objects.all(),
    )
    time_start = serializers.TimeField(read_only=True)
    date = serializers.DateField(read_only=True)
    duration = serializers.DurationField(read_only=True)
    time_end = serializers.TimeField(read_only=True)
    class Meta:
        model = Booking
        fields = ['id','creator', 'date', 'cabinet', 'lesson', 'time_start', 'duration', 'time_end', 'writable']


