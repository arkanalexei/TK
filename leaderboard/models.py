from django.db import models
from django.contrib.auth.models import User
from requests import request
# Create your models here.

class Achiever(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rank = models.IntegerField(default=1)
    username = models.CharField(max_length=100)
    points = models.IntegerField(default=0)