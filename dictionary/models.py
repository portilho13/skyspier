from django.db import models

# Create your models here.


# Def Dict Model

class Aircraft(models.Model):
    icao24 = models.CharField(max_length=60, null=True, blank=True)
    registration = models.CharField(max_length=60, null=True, blank=True)
    manufacturericao = models.CharField(max_length=60, null=True, blank=True)
    manufacturername = models.CharField(max_length=60, null=True, blank=True)
    model = models.CharField(max_length=60, null=True, blank=True)
    typecode = models.CharField(max_length=60, null=True, blank=True)
    serialnumber = models.CharField(max_length=60, null=True, blank=True)
    linenumber = models.CharField(max_length=60, null=True, blank=True)
    icaoaircrafttype = models.CharField(max_length=60, null=True, blank=True)
    operator = models.CharField(max_length=60, null=True, blank=True)
    operatorcallsign = models.CharField(max_length=60, null=True, blank=True)
    operatoricao = models.CharField(max_length=60, null=True, blank=True)
    operatoriata = models.CharField(max_length=60, null=True, blank=True)
    owner = models.CharField(max_length=60, null=True, blank=True)
    testreg = models.CharField(max_length=60, null=True, blank=True)
    registered = models.CharField(max_length=60, null=True, blank=True)
    reguntil = models.CharField(max_length=60, null=True, blank=True)
    status = models.CharField(max_length=60, null=True, blank=True)
    built = models.CharField(max_length=60, null=True, blank=True)
    firstflightdate = models.CharField(max_length=60, null=True, blank=True)
    seatconfiguration = models.CharField(max_length=60, null=True, blank=True)
    engines = models.CharField(max_length=60, null=True, blank=True)
    modes = models.CharField(max_length=60, null=True, blank=True)
    adsb = models.CharField(max_length=60, null=True, blank=True)
    acars = models.CharField(max_length=60, null=True, blank=True)
    notes = models.CharField(max_length=60, null=True, blank=True)
    categoryDescription = models.CharField(max_length=60, null=True, blank=True)

    def serialize(self):
        return {
            "id": self.id,
            "icao24": self.icao24,
            "registration": self.registration,
            "operator": self.operator,
            "model": self.model
        }


