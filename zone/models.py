from django.db import models

class Weather(models.Model):
    conditions = models.CharField(
        max_length=50
    )
    wind = models.PositiveSmallIntegerField(
        default = 0,
    )
    rain = models.PositiveSmallIntegerField(
        default = 0,
    )
    snow = models.PositiveSmallIntegerField(
        default = 0,
    )
    lightning = models.PositiveSmallIntegerField(
        default = 0,
    )
    clouds = models.PositiveSmallIntegerField(
        default = 0,
    )

    def __str__(self):
        return self.conditions


class ZoneState(models.Model):
    tod = models.IntegerField(
        default = 900000,
    )
    weather = models.ForeignKey( Weather )


class Zone(models.Model):
    name = models.CharField(max_length=200)
    state = models.ForeignKey( ZoneState )
    biome = models.PositiveSmallIntegerField(
        default = 0,
    )
    day = models.PositiveIntegerField(
        default = 900000,
    )
    night = models.PositiveIntegerField(
        default = 900000,
    )


    def __str__(self):
        return self.name
