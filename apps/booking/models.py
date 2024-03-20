from django.db import models
from apps.lesson.models import Category, Lesson
from apps.user.models import User
from datetime import datetime


class Cabinet(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(
        max_length=1500,
        verbose_name="Cabinet details",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Cabinet'
        verbose_name_plural = 'Cabinets'

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
        super().save(*args, **kwargs)
