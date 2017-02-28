from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^', views.account_list, name='accountList'),
]

urlpatterns = format_suffix_patterns(urlpatterns)