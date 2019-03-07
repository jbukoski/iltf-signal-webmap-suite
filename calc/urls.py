from django.conf.urls import include, url
from djgeojson.views import GeoJSONLayerView
from . import views
from django.contrib.gis import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^legend/', views.legend_view, name='calc_legend'),
    url(r'^sumstats/', views.sumstats_view, name='calc_sumstats'),
]

