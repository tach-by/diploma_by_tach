from django.db import models
from apps.user.models import User, Pupil
from apps.category.models import Category


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
    group = models.BooleanField(default=False)
    pupils = models.ManyToManyField(Pupil)

    def __str__(self):
        return f"{self.teacher} {self.description[:15]}"

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'