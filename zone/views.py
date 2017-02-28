from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Zone, Weather
from .serializers import ZoneSerializer, WeatherSerializer

@api_view(['GET'])
def zone_list(request, format = None):
    """
    List all zones, or create a new zone.
    """
    if request.method == 'GET':
        zones = Zone.objects.all()
        serializer = ZoneSerializer(zones, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def weather_list(request, format = None):
    """
    List all weathers, or create a new weather.
    """
    if request.method == 'GET':
        weathers = Weather.objects.all()
        serializer = WeatherSerializer(weathers, many=True)
        return Response(serializer.data)
