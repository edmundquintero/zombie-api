from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from zombie.models import Player, Item
from zombie.serializers import PlayerSerializer, ItemSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the Zombies index.")

# Create your views here.

@api_view(['GET'])
def player_list(request, format = None):
    """
    List all players, or create a new player.
    """
    if request.method == 'GET':
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def item_list(request, format = None):
    """
    List all items, or create a new item.
    """
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


