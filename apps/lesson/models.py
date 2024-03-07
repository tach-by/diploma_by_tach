from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(
        max_length=25,
        unique=True
    )
    description = models.TextField(
        max_length=1500,
        verbose_name="Описание",
    )
    durations=models.DurationField()
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
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        editable=False
    )


class Grouplesson(Lesson):
    pupils=models.ManyToManyField(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='group_lessons')