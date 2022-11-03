from django.db import models
from django.conf import settings

# Create your models here.
class Tukarpoin(models.Model):
    #user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True)
    points = models.IntegerField()
    voucher = models.TextField()