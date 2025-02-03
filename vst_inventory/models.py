from django.db import models

# Create your models here.

class MainDb(models.Model):
    iccid1 = models.CharField(max_length=50, blank=False)
    imsi1 = models.CharField(max_length=50, blank=False)
    msisdn1 = models.CharField(max_length=50, blank=False)
    iccid2 = models.CharField(max_length=50, blank=False)
    imsi2 = models.CharField(max_length=50, blank=False)
    msisdn2 = models.CharField(max_length=50, blank=False)
    imei = models.CharField(max_length=50, blank=False)
    serial = models.CharField(max_length=50, blank=False)
    activation = models.CharField(max_length=50, blank=False)
    expiry = models.DateField()
