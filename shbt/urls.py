from django.conf.urls import include, url
from djgeojson.views import GeoJSONLayerView
from . import views
from django.contrib.gis import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='shbt_index'),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}),
    url(r'^sample_up/', views.sample_up_view, name='shbt_sample_up'),
    url(r'^render_geojson/', views.render_geojson_view, name='render_geojson'),
    url(r'^download_single/', views.download_single_view, name='shbt_download_single'),
    url(r'^delete_single/', views.delete_single_view, name='shbt_delete_single'),
    url(r'^delete_up/', views.delete_up_view, name='shbt_delete_up'),
    url(r'^legend/', views.legend_view, name='legend'),
    url(r'^sumstats/', views.sumstats_view, name='sumstats'),
    url(r'^admin/logout/$', views.signout_view, name='signout'),
    url(r'^shbt_landfire_dl/$', views.shbt_landfire_dl_view, name = 'shbt_landfire_dl'),
    url(r'^shbt_ndvi_2005_dl/$', views.shbt_ndvi_2005_dl_view, name = 'shbt_ndvi_2005_dl'),
    url(r'^shbt_ndvi_2010_dl/$', views.shbt_ndvi_2010_dl_view, name = 'shbt_ndvi_2010_dl'),
    url(r'^shbt_ndvi_2015_dl/$', views.shbt_ndvi_2015_dl_view, name = 'shbt_ndvi_2015_dl'),
    url(r'^shbt_agc_dl/$', views.shbt_agc_dl_view, name = 'shbt_agc_dl'),
    url(r'^shbt_bgc_dl/$', views.shbt_bgc_dl_view, name = 'shbt_bgc_dl'),
    url(r'^shbt_soc_dl/$', views.shbt_soc_dl_view, name = 'shbt_soc_dl'),
    url(r'^boundary/', views.boundary_view, name = 'shbt_boundary'),
    url(r'^boundary_dl/', views.boundary_view_dl, name = 'shbt_boundary_dl'),
    url(r'^buff_bndry/', views.buff_bndry_view, name = 'shbt_buff_bndry'),
    url(r'^buff_bndry_dl/', views.buff_bndry_view_dl, name = 'shbt_buff_bndry_dl'),
    url(r'^counties/', views.counties_view, name = 'shbt_counties'),
    url(r'^counties_dl/', views.counties_view_dl, name = 'shbt_counties_dl'),
    url(r'^districts/', views.districts_view, name = 'shbt_districts'),
    url(r'^districts_dl/', views.districts_view_dl, name = 'shbt_districts_dl'),
    url(r'^nsi_flowlines/', views.nsi_flowlines_view, name = 'shbt_nsi_flowlines'),
    url(r'^nsi_flowlines_dl/', views.nsi_flowlines_view_dl, name = 'shbt_nsi_flowlines_dl'),
    url(r'^ownership/', views.ownership_view, name = 'shbt_ownership'),
    url(r'^ownership_dl/', views.ownership_view_dl, name = 'shbt_ownership_dl'),
    url(r'^range_units/', views.range_units_view, name = 'shbt_range_units'),
    url(r'^range_units_dl/', views.range_units_view_dl, name = 'shbt_range_units_dl'),
    url(r'^document/', views.document_view, name = 'shbt_document'),
    url(r'^document_dl/', views.document_view_dl, name = 'shbt_document_dl'),

]
