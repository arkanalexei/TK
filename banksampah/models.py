from django.db import models
from django.conf import settings

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
    # type = ???? TODO