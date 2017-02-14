from django.conf.urls import url
from . import views
from comanche.models import counties, cotton, caddo
from django.contrib.gis import admin
from djgeojson.views import GeoJSONLayerView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^counties/', GeoJSONLayerView.as_view(model=counties), name='counties'),
    url(r'^cotton/', GeoJSONLayerView.as_view(model=cotton), name='cotton'),
]
