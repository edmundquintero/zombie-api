from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^players/$', views.player_list, name='playerList'),
    url(r'^01/$', views.item_list, name='itemList'),
    url(r'^inventories/$', views.inventory_list, name='inventoryList'),
]

urlpatterns = format_suffix_patterns(urlpatterns)