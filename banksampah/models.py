from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
# TODO: migrate

class WasteDeposit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    mass = models.FloatField()
    description = models.TextField()
    date_time = models.DateField(default=timezone.now)
    # type = ???? TODO