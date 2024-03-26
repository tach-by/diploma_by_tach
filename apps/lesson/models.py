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
    pupil = models.ForeignKey(
        Pupil,
        verbose_name='pupil',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.teacher} {self.pupil} {self.category}"

    @property
    def get_full_name(self):
        return f"{self.teacher} {self.pupil} {self.category}"

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'