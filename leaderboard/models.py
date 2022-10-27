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

# belum migrate
class Feedback(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True  
    )
    feedback = models.TextField()
    date_time = models.DateField(auto_now_add=True)