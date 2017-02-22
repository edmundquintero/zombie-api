from rest_framework import serializers

from zombie.models import Player, Item


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('player_name',)

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'