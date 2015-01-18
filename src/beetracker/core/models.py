from django.db import models

# Create your models here.
from decimal import Decimal, ROUND_DOWN

from django.db.models import Q
from  datetime import datetime
from django.utils.encoding import python_2_unicode_compatible

from django.contrib.auth.models import User

#
# python_2_unicode_compatible
#
# https://docs.djangoproject.com/en/1.7/ref/utils/#django.utils.encoding.python_2_unicode_compatible#



@python_2_unicode_compatible
class Apiary(models.Model):
    """
    Company model
    """
 
    owner = models.ForeignKey(User, related_name="apiaries")
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
    latitude = models.DecimalField (max_digits=30, decimal_places=20)
    longitude = models.DecimalField (max_digits=30, decimal_places=20)
    
    latitude_approx = models.DecimalField (max_digits=30, decimal_places=20, default=0)
    longitude_approx = models.DecimalField (max_digits=30, decimal_places=20, default=0)
    

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.latitude_approx = (self.latitude / 2).quantize(Decimal('.01'), rounding=ROUND_DOWN) * 2
        self.longitude_approx = (self.longitude /2).quantize(Decimal('.01'), rounding=ROUND_DOWN)*2
        super(Apiary, self).save(*args, **kwargs)


    def get_current_hives(self):
        #self.placement.filter(start_date__lt=now, end_date__gt=now).hive.all()
        return Hive.objects.filter(placement__apiary = self).filter(Q(placement__start_date__lt=datetime.now()) | Q(placement__start_date__isnull=True),
                        Q(placement__end_date__lt=datetime.now()) | Q(placement__end_date__isnull=True))







@python_2_unicode_compatible
class HAPlacement(models.Model):
    apiary = models.ForeignKey('Apiary', related_name="placement")
    hive = models.ForeignKey('Hive', related_name="placement")
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{0} - {1}".format(self.apiary, self.hive)



@python_2_unicode_compatible
class Hive(models.Model):
    """
    Company model
    """
    identifier = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
       

    def __str__(self):
        return self.identifier



@python_2_unicode_compatible
class MapInformation(models.Model):
    apiary = models.ForeignKey('Apiary')
    date = models.DateTimeField(blank=True, null=True)
    
    tag_key = models.CharField(max_length=255)
    tag_value = models.CharField(max_length=255)
    api_response = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return "{0} - {1}/{2}".format(self.apiary, self.tag_key, self.tag_value)

    class Meta:
        get_latest_by = "date"


@python_2_unicode_compatible
class ActivityIndication(models.Model):
    hive = models.ForeignKey('Hive', related_name="activityindication")
    datetime = models.DateTimeField(blank=True, null=True)
    
    index = models.IntegerField()
    
    def __str__(self):
        return "{0} - {1}".format(self.hive, str(self.datetime))





@python_2_unicode_compatible
class WhatToDoSeason(models.Model):
    kw_start = models.IntegerField()
    kw_end = models.IntegerField()

    headline = models.CharField(max_length=255)
    copy = models.TextField(max_length=255)
   