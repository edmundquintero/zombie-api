from rest_framework import serializers

from zombie.models import Player, Item, Inventory

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    slot0 = ItemSerializer(many=True, read_only=True)
    slot1 = ItemSerializer(many=True, read_only=True)
    slot2 = ItemSerializer(many=True, read_only=True)
    slot3 = ItemSerializer(many=True, read_only=True)
    slot4 = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Inventory
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    inventory = InventorySerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = ('player_name', 'inventory')


