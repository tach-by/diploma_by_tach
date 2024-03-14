from django.db import models
from apps.lesson.models import Category, Lesson
from datetime import datetime


class Cabinet(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(
        max_length=1500,
        verbose_name="Cabinet details",
        default="")

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
    time_start = models.TimeField()  #если тут unique_for_date=True то летят ошибки
    duration = models.DurationField(
        null=True,
        blank=True
    )
    time_end = models.TimeField(
        null=True,
        blank=True
    )
    repeat = models.BooleanField(default=False)
    writable = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.duration:
            self.duration = self.lesson.category.duration * 60       #convert to minuts
        else:
            self.duration = self.duration * 60
        start_datetime = datetime.combine(self.date, self.time_start)

        end_datetime = start_datetime + self.duration

        self.time_end = end_datetime.time()
        super().save(*args, **kwargs)
