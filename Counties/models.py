from django.db import models
from django.contrib.postgres.fields import ArrayField


class Counties(models.Model):
    county = models.CharField(max_length=100)
    places = ArrayField( models.CharField( max_length=100 ), blank=True )

    def __str__(self):
        return self.county