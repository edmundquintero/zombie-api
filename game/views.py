from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Game
from .serializers import GameSerializer

@api_view(['GET'])
def game_list(request, format = None):
    """
    List all games, or create a new game.
    """
    if request.method == 'GET':
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
