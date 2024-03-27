from django.db import models
from apps.lesson.models import Lesson
from apps.user.models import User
from datetime import datetime
from apps.cabinet.models import Cabinet


class Booking(models.Model):
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    cabinet = models.ForeignKey(
        Cabinet,
        on_delete=models.CASCADE
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        null=True,
        blank=True

    )
    time_start = models.TimeField()
    duration = models.DurationField(
        null=True,
        blank=True,
        help_text="In format DD HH:MM:SS"
    )
    time_end = models.TimeField(
        null=True,
        blank=True
    )
    repeat = models.BooleanField(default=False)
    writable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.creator} {self.date} {self.time_start}"

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def save(self, *args, **kwargs):
        if not self.duration:
            self.duration = self.lesson.category.duration

        start_datetime = datetime.combine(self.date, self.time_start)

        end_datetime = start_datetime + self.duration

        self.time_end = end_datetime.time()

        if not self.lesson:
            self.writable = True
        boks = Booking.objects.filter(cabinet=self.cabinet, date=self.date)
        for bok in boks:
            if (bok.time_start <= self.time_start < bok.time_end) or (bok.time_start < self.time_end <= bok.time_end):
                return "Время недоступно для записи"
        super().save(*args, **kwargs)
