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
    STATUS = models.CharField(max_length=50,blank=False,choices=choices,default='INACTIVE')
    
class Branch1(models.Model):
    ICCID1 = models.CharField(max_length=50,blank=False)
    MSISDN1 = models.CharField(max_length=50,blank=False)
    choices = (
        ('ACTIVE','active'),
        ('INACTIVE','not active'),
    )
    STATUS = models.CharField(max_length=50,blank=False,choices=choices,default='INACTIVE')
    
class Branch2(models.Model):
    ICCID2 = models.CharField(max_length=50,blank=False)
    MSISDN2 = models.CharField(max_length=50,blank=False)
    choices = (
        ('ACTIVE','active'),
        ('INACTIVE','not active'),
    )
    STATUS = models.CharField(max_length=50,blank=False,choices=choices,default='INACTIVE')
    
class Branch3(models.Model):
    ICCID1 = models.CharField(max_length=50,blank=False)
    IMEI = models.CharField(max_length=50,blank=False)
    SERIAL = models.CharField(max_length=50,blank=False)
    choices = (
        ('ACTIVE','active'),
        ('INACTIVE','not active'),
    )
    STATUS = models.CharField(max_length=50,blank=False,choices=choices,default='INACTIVE')
    
    
    
    
