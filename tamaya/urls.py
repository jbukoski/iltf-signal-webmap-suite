from django.conf.urls import include, url
from djgeojson.views import GeoJSONLayerView
from . import views
from django.contrib.gis import admin

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^boundary/', views.boundary_view, name='boundary'),
    url(r'^mbls/', views.mbls_view, name='mbls'),
    url(r'^roads/', views.roads_view, name='roads'),
    url(r'^soil_data/', views.soil_data_view, name='soil_data'),
    url(r'^user_pts/', views.user_points_view, name='user_points'),
    url(r'^user_lines/', views.user_lines_view, name='user_lines'),
    url(r'^user_polygons/', views.user_polygons_view, name='user_polygons'),
    url(r'^bd_download/', views.bd_dl_view, name='boundary_dl'),
    url(r'^ph_download/', views.ph_dl_view, name='ph_dl'),
]
