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
    date= models.DateField()
    cabinet=models.ForeignKey(Cabinet, on_delete=models.CASCADE)
    lesson=models.ForeignKey(Lesson, on_delete=models.CASCADE)
    time_start=models.TimeField(unique_for_date=True)  #если тут unique_for_date=True то летят ошибки
    duration=models.DurationField
    time_end=models.TimeField()
    repeat= models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.duration = self.lesson.category.duration * 60       #convert to minuts

        start_datetime = datetime.combine(self.date, self.time_start)

        end_datetime = start_datetime + self.duration

        self.time_end = end_datetime.time()
        super().save(*args, **kwargs)
