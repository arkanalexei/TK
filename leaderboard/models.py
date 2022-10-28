from email.policy import default
from django.db import models
from django.conf import settings


# Create your models here.

class Achiever(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True  
    )
    points = models.IntegerField(default=0)


class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True  
    )
    comment = models.TextField()
    date_time = models.DateField(auto_now_add=True)