from django.db import models
from apps.lesson.models import Category, Lesson


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
    time_start=models.TimeField(unique_for_date=True)
    duration=models.DurationField
    time_end=models.TimeField()
    repeat= models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.duration = self.lesson.category.duration
        self.time_end = self.time_start + self.duration
        super().save(*args, **kwargs)
