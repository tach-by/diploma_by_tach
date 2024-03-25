from django.db import models


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
