from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=200)
    duration = models.DurationField(
        default = 0
    )
    currentZone = models.ForeignKey(
        'zone.Zone',
        models.SET_NULL,
        blank = True,
        null = True,
    )
    player = models.ForeignKey(
        'player.Player',
        models.SET_NULL,
        blank = True,
        null = True,
    )
    difficulty = models.IntegerField(
        default = 1,
    )
    steps = models.IntegerField(
        default = 0,
    )
    jumps = models.IntegerField(
        default = 0,
    )
    enemiesSpotted = models.IntegerField(
        default = 0,
    )
    safeAreas = models.IntegerField(
        default = 0,
    )
    encounters = models.IntegerField(
        default = 0,
    )
    zones = models.IntegerField(
        default = 0,
    )
    kills = models.IntegerField(
        default = 0,
    )


    def __str__(self):
        return self.name
