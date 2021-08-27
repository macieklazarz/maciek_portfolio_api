from django.conf.urls import url, include
from . import views
from django.urls import path


app_name = 'tuzy'

urlpatterns = [
    url(r'^$', views.tuzy_lista, name="lista"),
    url(r'^(?P<slug>[\w-]+)/$', views.tuz, name="tuz"),


]
