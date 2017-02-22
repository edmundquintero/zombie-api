from django.db import models

class Player(models.Model):
    player_name = models.CharField(max_length=200)

    def __str__(self):
        return self.player_name

class Item(models.Model):
    name = models.CharField(max_length=50)
    dmg = models.IntegerField(default = 0)
    heal = models.IntegerField(default = 0)

    def __str__(self):
        return self.name + ' - (dmg: ' + str(self.dmg) + ' / heal: ' + str(self.heal) + ' )'