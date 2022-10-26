from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
# TODO: migrate

class WasteDeposit(models.Model):
    CHOICES = (
            ("PLASTIK", "Plastik"),
            ("KACA", "Kaca / Beling"),
            ("KERTAS", "Kertas / Kardus"),
            ("ETC", "Organik & Lainnya")
        )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    mass = models.FloatField()
    description = models.TextField()
    date_time = models.DateField(default=timezone.now)
    type = models.CharField(max_length=32, choices=CHOICES, default=CHOICES[0])

class News(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(default=timezone.now)
    title = models.CharField(max_length=255)
    description = models.TextField()
