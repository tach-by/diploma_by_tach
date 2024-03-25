from django.db import models


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

# Create your models here.
