from django.conf.urls import include, url
from djgeojson.views import GeoJSONLayerView
from . import views
from django.contrib.gis import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='jskt_index'),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}),
    url(r'^boundary/', views.boundary_view, name='jskt_boundary'),
    url(r'^buff_bndry/', views.buff_bndry_view, name='jskt_buff_bndry'),
    url(r'^boundary_dl/', views.boundary_view_dl, name='jst_boundary_dl'),
    url(r'^jefco_parcels_dl/', views.jefco_parcels_view_dl, name='jst_jefco_parcels_dl'),
    url(r'^jst_boundary_clco_dl/', views.jst_boundary_clco_view_dl, name='jst_boundary_clco_dl'),
    url(r'^jst_trust_parcels_clco_dl/', views.jst_trust_parcels_clco_view_dl, name='jst_trust_parcels_clco_dl'),
    url(r'^jst_land_consol_area_dl/', views.jst_land_consol_area_view_dl, name='jst_land_consol_area_dl'),
    url(r'^jst_reservation_parcels_clco_dl/', views.jst_reservation_parcels_clco_view_dl, name='jst_reservation_parcels_clco_dl'),
    url(r'^clco_parcels_dl/', views.clco_parcels_view_dl, name='jst_clco_parcels_dl'),
    url(r'^jst_boundary_jefco_dl/', views.jst_boundary_jefco_view_dl, name='jst_boundary_jefco_dl'),
    url(r'^jst_fee_parcels_clco_dl/', views.jst_fee_parcels_clco_view_dl, name='jst_fee_parcels_clco_dl'),
    url(r'^jst_landfire_dl/$', views.jst_landfire_dl_view, name = 'jst_landfire_dl'),
    url(r'^jst_ndvi_2005_dl/$', views.jst_ndvi_2005_dl_view, name = 'jst_ndvi_2005_dl'),
    url(r'^jst_ndvi_2010_dl/$', views.jst_ndvi_2010_dl_view, name = 'jst_ndvi_2010_dl'),
    url(r'^jst_ndvi_2015_dl/$', views.jst_ndvi_2015_dl_view, name = 'jst_ndvi_2015_dl'),
    url(r'^jst_agc_dl/$', views.jst_agc_dl_view, name = 'jst_agc_dl'),
    url(r'^jst_bgc_dl/$', views.jst_bgc_dl_view, name = 'jst_bgc_dl'),
    url(r'^jst_soc_dl/$', views.jst_soc_dl_view, name = 'jst_soc_dl'),
    url(r'^sample_up/', views.sample_up_view, name='jskt_sample_up'),
    url(r'^render_geojson/', views.render_geojson_view, name='render_geojson'),
    url(r'^download_single/', views.download_single_view, name="jskt_download_single"),
    url(r'^delete_single/', views.delete_single_view, name="jskt_delete_single"),
    url(r'^delete_up/', views.delete_up_view, name='jskt_delete_up'),
    url(r'^admin/logout/$', views.signout_view, name='signout'),
]
