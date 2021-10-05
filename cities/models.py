from django.db import models

from cities.querysets import CityQuerySet
from . import utils

class CountryName(models.Model):
    id=models.AutoField(primary_key=True)
    Country=models.CharField(max_length=254,null=True)
    Region=models.CharField(max_length=254,null=True)
    Population=models.IntegerField(null=True,blank=True)
    Area=models.IntegerField(null=True,blank=True)
    Pop_Density=models.CharField(max_length=100,null=True,blank=True)
    Coastline=models.CharField(max_length=100,null=True,blank=True) 
    Net_migration=models.CharField(max_length=100,null=True,blank=True)
    Infant_mortality=models.CharField(max_length=100,null=True,blank=True)
    GDP=models.CharField(max_length=100,null=True,blank=True)
    Literacy=models.CharField(max_length=100,null=True,blank=True)
    Phones=models.IntegerField(null=True,blank=True)
    Arable=models.CharField(max_length=100,null=True,blank=True)
    Crops=models.CharField(max_length=100,null=True,blank=True)
    Other=models.CharField(max_length=100,null=True,blank=True)
    Climate=models.CharField(max_length=200,null=True,blank=True)
    Birthrate=models.CharField(max_length=100,null=True,blank=True)
    Deathrate=models.CharField(max_length=100,null=True,blank=True)
    Agriculture=models.CharField(max_length=100,null=True,blank=True)
    Industry=models.CharField(max_length=100,null=True,blank=True)
    Service=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.Country

    class Meta:
        ordering = ["Country"]




class State(models.Model):    
    code = models.IntegerField()
    name = models.CharField(max_length=500)
    abbr = models.CharField(max_length=10)

    class Meta:
        ordering = ["name"]
    def __str__(self):
        return self.name


class City(models.Model):
    state = models.ForeignKey(State,null=True, blank=True, on_delete=models.CASCADE)    
    code = models.IntegerField()
    name = models.CharField(max_length=150)
    search_name = models.CharField(db_index=True, max_length=150)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
   

    objects = CityQuerySet.as_manager()

    class Meta:
        ordering = ["search_name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.search_name = utils.clear_text(self.name).lower()
        super(City, self).save(*args, **kwargs)
