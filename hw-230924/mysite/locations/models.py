from django.db import models

# Create your models here.
class LocationInfo(models.Model):
    name = models.CharField(max_length=80)
    loc_x = models.FloatField(max_length=16)
    loc_y = models.FloatField(max_length=16)
    description = models.TextField(max_length=500)