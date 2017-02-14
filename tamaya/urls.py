from django.conf.urls import include, url
from djgeojson.views import GeoJSONLayerView
from . import views
from tamaya.models import boundary, mbls, roads
from django.contrib.gis import admin

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^boundary/', views.boundary_view, name='boundary'),
    url(r'^mbls/', GeoJSONLayerView.as_view(model=mbls), name='mbls'),
    url(r'^roads/', GeoJSONLayerView.as_view(model=roads), name='roads'),
    url(r'^bulk_density/', views.bulk_density_view, name='bulk_density'),

]
