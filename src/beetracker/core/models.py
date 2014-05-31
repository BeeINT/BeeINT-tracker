from django.db import models

# Create your models here.




class Apiary(models.Model):
    """
    Company model
    """
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
    latitude = models.DecimalField (max_digits=30, decimal_places=20)
    longitude = models.DecimalField (max_digits=30, decimal_places=20)
    
    def __unicode__(self):
    	return self.name




class HAPlacement(models.Model):
	apiary = models.ForeignKey('Apiary', related_name="placement")
	hive = models.ForeignKey('Hive', related_name="placement")
	start_date = models.DateTimeField(blank=True, null=True)
	end_date = models.DateTimeField(blank=True, null=True)


class Hive(models.Model):
    """
    Company model
    """
    identifier = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
       

    def __unicode__(self):
    	return self.identifier



class MapInformation(models.Model):
	apiary = models.ForeignKey('Apiary')
	date = models.DateTimeField(blank=True, null=True)
	
	tag_key = models.CharField(max_length=255)
	tag_value = models.CharField(max_length=255)
	api_response = models.TextField(blank=True, null=True)
	