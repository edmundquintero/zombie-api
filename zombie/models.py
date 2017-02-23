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


class Inventory(models.Model):
    name = models.CharField(max_length=50)
    player = models.ForeignKey(Player, related_name='inventory', on_delete=models.CASCADE)
    slot0 = models.ManyToManyField(Item, related_name='slot0')
    slot1 = models.ManyToManyField(Item, related_name='slot1')
    slot2 = models.ManyToManyField(Item, related_name='slot2')
    slot3 = models.ManyToManyField(Item, related_name='slot3')
    slot4 = models.ManyToManyField(Item, related_name='slot4')

    def __str__(self):
        return self.name
