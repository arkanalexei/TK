from email.policy import default
from django.db import models
from django.conf import settings
from requests import request


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
        blank=True,
        related_name='comments'  
    )
    comment = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.username, self.comment)