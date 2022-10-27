from django.db import models
from django.conf import settings
from django.utils import timezone

class News(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(default=timezone.now)
    title = models.CharField(max_length=255)
    description = models.TextField()