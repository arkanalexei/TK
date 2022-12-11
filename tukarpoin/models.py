from django.db import models
from django.conf import settings

# Create your models here.
class Perks(models.Model):
    nama = models.CharField(max_length=250)
    deskripsi = models.TextField()
    harga = models.IntegerField()