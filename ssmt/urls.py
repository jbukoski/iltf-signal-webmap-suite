from django.conf.urls import include, url
from djgeojson.views import GeoJSONLayerView
from . import views
from django.contrib.gis import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='ssmt_index'),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}),
    url(r'^sample_up/', views.sample_up_view, name='sample_up'),
    url(r'^render_geojson/', views.render_geojson_view, name='render_geojson'),
    url(r'^download_single/', views.download_single_view, name='download_single'),
    url(r'^delete_single/', views.delete_single_view, name='delete_single'),
    url(r'^delete_up/', views.delete_up_view, name='delete_up'),
    url(r'^legend/', views.legend_view, name='legend'),
    url(r'^sumstats/', views.sumstats_view, name='sumstats'),
    url(r'^admin/logout/$', views.signout_view, name='signout'),
    url(r'^boundary/', views.boundary_view, name = 'ssmt_boundary'),
    url(r'^boundary_dl/', views.boundary_view_dl, name = 'ssmt_boundary_dl'),
    url(r'^buff_bndry/', views.buff_bndry_view, name = 'ssmt_buff_bndry'),
    url(r'^buff_bndry_dl/', views.buff_bndry_view_dl, name = 'ssmt_buff_bndry_dl'),
    url(r'^ceded_territories/', views.ceded_territories_view, name = 'ssmt_ceded_territories'),
    url(r'^ceded_territories_dl/', views.ceded_territories_view_dl, name = 'ssmt_ceded_territories_dl'),
    url(r'^parcels/', views.parcels_view, name = 'ssmt_parcels'),
    url(r'^parcels_dl/', views.parcels_view_dl, name = 'ssmt_parcels_dl'),
    url(r'^tax_areas/', views.tax_areas_view, name = 'ssmt_tax_areas'),
    url(r'^tax_areas_dl/', views.tax_areas_view_dl, name = 'ssmt_tax_areas_dl'),
    url(r'^units/', views.units_view, name = 'ssmt_units'),
    url(r'^units_dl/', views.units_view_dl, name = 'ssmt_units_dl'),
    url(r'^document/', views.document_view, name = 'ssmt_document'),
    url(r'^document_dl/', views.document_view_dl, name = 'ssmt_document_dl'),

]
