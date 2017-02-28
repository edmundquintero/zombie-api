from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=200)
    health = models.PositiveSmallIntegerField(
        default = 100,
    )

    def __str__(self):
        return self.name

