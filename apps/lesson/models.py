from django.db import models
from apps.user.models import User, Pupil

class Category(models.Model):
    name = models.CharField(
        max_length=25,
        unique=True
    )
    description = models.TextField(
        max_length=1500,
        verbose_name="Описание",
    )
    duration=models.DurationField()
    price=models.IntegerField(blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Lesson(models.Model):
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        editable=False
    )
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )


class Individuallesson(Lesson):
    pupil=models.ForeignKey(
        Pupil,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        editable=False
    )


class Grouplesson(Lesson):
    pupils=models.ManyToManyField(
        Pupil,
        through='Attendance'
    )


class Attendance(models.Model):
    date = models.DateField()
    pupil = models.ForeignKey(Pupil, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Grouplesson, on_delete=models.CASCADE)
    attended = models.BooleanField(default=True)