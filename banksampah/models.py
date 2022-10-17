from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User

# Create your models here.
# TODO: migrate

class WasteDeposit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    mass = models.FloatField()
    description = models.TextField()
    date_time = models.DateTimeField()
    type = models.CharField(max_length=32, choices=(
            ("PLASTIK", "Plastik"),
            ("KACA", "Kaca / Beling"),
            ("KERTAS", "Kertas / Kardus"),
            ("ETC", "Organik & Lainnya")
        )
    )