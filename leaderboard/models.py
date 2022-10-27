from django.db import models
from django.db.models import Model
from django.conf import settings
# Create your models here.

class Achiever(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        points = models.IntegerField()
    )