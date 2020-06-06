#!/bin/sh

TRIBE=$1

echo "from django.conf.urls import include, url
from djgeojson.views import GeoJSONLayerView
from . import views
from django.contrib.gis import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='${TRIBE}_index'),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}),
    url(r'^sample_up/', views.sample_up_view, name='${TRIBE}_sample_up'),
    url(r'^render_geojson/', views.render_geojson_view, name='render_geojson'),
    url(r'^download_single/', views.download_single_view, name='${TRIBE}_download_single'),
    url(r'^delete_single/', views.delete_single_view, name='${TRIBE}_delete_single'),
    url(r'^delete_up/', views.delete_up_view, name='${TRIBE}_delete_up'),
    url(r'^legend/', views.legend_view, name='legend'),
    url(r'^sumstats/', views.sumstats_view, name='sumstats'),
    url(r'^admin/logout/$', views.signout_view, name='signout'),
    url(r'^${TRIBE}_landfire_dl/$', views.${TRIBE}_landfire_dl_view, name = '${TRIBE}_landfire_dl'),
    url(r'^${TRIBE}_ndvi_2005_dl/$', views.${TRIBE}_ndvi_2005_dl_view, name = '${TRIBE}_ndvi_2005_dl'),
    url(r'^${TRIBE}_ndvi_2010_dl/$', views.${TRIBE}_ndvi_2010_dl_view, name = '${TRIBE}_ndvi_2010_dl'),
    url(r'^${TRIBE}_ndvi_2015_dl/$', views.${TRIBE}_ndvi_2015_dl_view, name = '${TRIBE}_ndvi_2015_dl'),
    url(r'^${TRIBE}_agc_dl/$', views.${TRIBE}_agc_dl_view, name = '${TRIBE}_agc_dl'),
    url(r'^${TRIBE}_bgc_dl/$', views.${TRIBE}_bgc_dl_view, name = '${TRIBE}_bgc_dl'),
    url(r'^${TRIBE}_soc_dl/$', views.${TRIBE}_soc_dl_view, name = '${TRIBE}_soc_dl')," > ../$TRIBE/urls.py

# Generate model-specific URLs

PY_MODELS=$(python ../manage.py shell -c " 

from django.apps import apps
from django.contrib import admin

mods = apps.all_models['$TRIBE']

empty = ''
for i in mods.keys():
    empty += i+' '

print(empty)

")

# Convert to bash array and write to the python file

MODELS=( $PY_MODELS )

for i in "${MODELS[@]}"; do
    echo "    url(r'^$i/', views.${i}_view, name = '${TRIBE}_${i}'),
    url(r'^${i}_dl/', views.${i}_view_dl, name = '${TRIBE}_${i}_dl')," >> ../$TRIBE/urls.py
done


echo '
]' >> ../$TRIBE/urls.py

