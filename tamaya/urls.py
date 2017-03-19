from django.conf.urls import include, url
from djgeojson.views import GeoJSONLayerView
from . import views
from tamaya.models import boundary, mbls, roads
from django.contrib.gis import admin

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^boundary/', views.boundary_view, name='boundary'),
    url(r'^mbls/', views.mbls_view, name='mbls'),
    url(r'^roads/', views.roads_view, name='roads'),
    url(r'^soil_data/', views.soil_data_view, name='soil_data'),
    url(r'^user_pts/', views.user_points_view, name='user_points'),
]
