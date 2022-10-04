from django.db import models

# Create your models here.

class Items(models.Model):
    ICCID1 = models.CharField(max_length=50,blank=False)
    IMSI1 = models.CharField(max_length=50,blank=False)
    MSISDN1 = models.CharField(max_length=50,blank=False)
    ICCID2 = models.CharField(max_length=50,blank=False)
    IMSI2 = models.CharField(max_length=50,blank=False)
    MSISDN2 = models.CharField(max_length=50,blank=False)
    IMEI = models.CharField(max_length=50,blank=False)
    choices = (
        ('ACTIVE','active'),
        ('INACTIVE','not active'),
    )
    ACTIVATION = models.DateTimeField()
    EXPIRY = models.DateTimeField()
    STATUS = models.CharField(max_length=50,blank=False,choices=choices,default='INACTIVE')
    
class Branch1(models.Model):
    iccid1 = models.CharField(max_length=50,blank=False)
    msisdn1 = models.CharField(max_length=50,blank=False)
    choices = (
        ('ACTIVE','active'),
        ('INACTIVE','not active'),
    )
    status = models.CharField(max_length=50,blank=False,choices=choices,default='INACTIVE')
    
class Branch2(models.Model):
    iccid2 = models.CharField(max_length=50,blank=False)
    msisdn2 = models.CharField(max_length=50,blank=False)
    choices = (
        ('ACTIVE','active'),
        ('INACTIVE','not active'),
    )
    status = models.CharField(max_length=50,blank=False,choices=choices,default='INACTIVE')
    
class Branch3(models.Model):
    iccid1 = models.CharField(max_length=50,blank=False)
    imei = models.CharField(max_length=50,blank=False)
    serial = models.CharField(max_length=50,blank=False)
    choices = (
        ('ACTIVE','active'),
        ('INACTIVE','not active'),
    )
    status = models.CharField(max_length=50,blank=False,choices=choices,default='INACTIVE')
    
    
    
    
