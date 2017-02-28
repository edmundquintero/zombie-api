from django.contrib import admin

from .models import Zone, Weather, ZoneState

admin.site.register(Zone)
admin.site.register(ZoneState)

admin.site.register(Weather)
