from django.db import models
from apps.user.models import User, Pupil
# from apps.booking.models import Booking


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
        verbose_name='Creator'
    )
    teacher = models.ForeignKey(
        User,
        verbose_name='teacher',
        related_name="teacher",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    description = models.TextField(
        max_length=1500,
        verbose_name="Описание",
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'


class Individuallesson(Lesson):
    pupil=models.ForeignKey(
        Pupil,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.creator} {self.pupil}"

    class Meta:
        verbose_name = 'Individual lesson'
        verbose_name_plural = 'Individual lessons'


class Grouplesson(Lesson):
    pupils = models.ManyToManyField(Pupil)

    def __str__(self):
        return f"{self.creator} {self.category}"

    class Meta:
        verbose_name = 'Group lesson'
        verbose_name_plural = 'Group lessons'


# class Attendance(models.Model):
#     booking= models.ForeignKey(Booking, on_delete=models.CASCADE)
#     pupil = models.ForeignKey(Pupil, on_delete=models.CASCADE)
#     attended = models.BooleanField(default=True)


