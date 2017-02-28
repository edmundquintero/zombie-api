from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Player
from .serializers import PlayerSerializer

@api_view(['GET'])
def player_list(request, format = None):
    """
    List all players, or create a new player.
    """
    if request.method == 'GET':
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

