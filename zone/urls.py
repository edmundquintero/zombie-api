from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^', views.zone_list, name='zoneList'),
    url(r'^/weather', views.weather_list, name='weatherList'),
]

urlpatterns = format_suffix_patterns(urlpatterns)