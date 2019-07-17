from django.conf.urls import include, url
from djgeojson.views import GeoJSONLayerView
from . import views
from django.contrib.gis import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='rcbc_index'),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}),
    url(r'^sample_up/', views.sample_up_view, name='sample_up'),
    url(r'^render_geojson/', views.render_geojson_view, name='render_geojson'),
    url(r'^download_single/', views.download_single_view, name='download_single'),
    url(r'^delete_single/', views.delete_single_view, name='delete_single'),
    url(r'^delete_up/', views.delete_up_view, name='delete_up'),
    url(r'^legend/', views.legend_view, name='legend'),
    url(r'^sumstats/', views.sumstats_view, name='sumstats'),
    url(r'^admin/logout/$', views.signout_view, name='signout'),
    url(r'^ashland_cnty/', views.ashland_cnty_view, name = 'rcbc_ashland_cnty'),
    url(r'^ashland_cnty_dl/', views.ashland_cnty_view_dl, name = 'rcbc_ashland_cnty_dl'),
    url(r'^bayfield_cnty/', views.bayfield_cnty_view, name = 'rcbc_bayfield_cnty'),
    url(r'^bayfield_cnty_dl/', views.bayfield_cnty_view_dl, name = 'rcbc_bayfield_cnty_dl'),
    url(r'^beachroute/', views.beachroute_view, name = 'rcbc_beachroute'),
    url(r'^beachroute_dl/', views.beachroute_view_dl, name = 'rcbc_beachroute_dl'),
    url(r'^boundary/', views.boundary_view, name = 'rcbc_boundary'),
    url(r'^boundary_dl/', views.boundary_view_dl, name = 'rcbc_boundary_dl'),
    url(r'^buff_bndry/', views.buff_bndry_view, name = 'rcbc_buff_bndry'),
    url(r'^buff_bndry_dl/', views.buff_bndry_view_dl, name = 'rcbc_buff_bndry_dl'),
    url(r'^claytoncreektrail/', views.claytoncreektrail_view, name = 'rcbc_claytoncreektrail'),
    url(r'^claytoncreektrail_dl/', views.claytoncreektrail_view_dl, name = 'rcbc_claytoncreektrail_dl'),
    url(r'^conservationmgmtarea/', views.conservationmgmtarea_view, name = 'rcbc_conservationmgmtarea'),
    url(r'^conservationmgmtarea_dl/', views.conservationmgmtarea_view_dl, name = 'rcbc_conservationmgmtarea_dl'),
    url(r'^easyroute/', views.easyroute_view, name = 'rcbc_easyroute'),
    url(r'^easyroute_dl/', views.easyroute_view_dl, name = 'rcbc_easyroute_dl'),
    url(r'^fbtnp/', views.fbtnp_view, name = 'rcbc_fbtnp'),
    url(r'^fbtnp_dl/', views.fbtnp_view_dl, name = 'rcbc_fbtnp_dl'),
    url(r'^frogbaytrails/', views.frogbaytrails_view, name = 'rcbc_frogbaytrails'),
    url(r'^frogbaytrails_dl/', views.frogbaytrails_view_dl, name = 'rcbc_frogbaytrails_dl'),
    url(r'^rc_zoning_districts/', views.rc_zoning_districts_view, name = 'rcbc_rc_zoning_districts'),
    url(r'^rc_zoning_districts_dl/', views.rc_zoning_districts_view_dl, name = 'rcbc_rc_zoning_districts_dl'),
    url(r'^s_fld_haz_ar/', views.s_fld_haz_ar_view, name = 'rcbc_s_fld_haz_ar'),
    url(r'^s_fld_haz_ar_dl/', views.s_fld_haz_ar_view_dl, name = 'rcbc_s_fld_haz_ar_dl'),
    url(r'^s_fld_haz_ln/', views.s_fld_haz_ln_view, name = 'rcbc_s_fld_haz_ln'),
    url(r'^s_fld_haz_ln_dl/', views.s_fld_haz_ln_view_dl, name = 'rcbc_s_fld_haz_ln_dl'),
    url(r'^s_trnsport_ln/', views.s_trnsport_ln_view, name = 'rcbc_s_trnsport_ln'),
    url(r'^s_trnsport_ln_dl/', views.s_trnsport_ln_view_dl, name = 'rcbc_s_trnsport_ln_dl'),
    url(r'^s_wtr_ar/', views.s_wtr_ar_view, name = 'rcbc_s_wtr_ar'),
    url(r'^s_wtr_ar_dl/', views.s_wtr_ar_view_dl, name = 'rcbc_s_wtr_ar_dl'),
    url(r'^s_wtr_ln/', views.s_wtr_ln_view, name = 'rcbc_s_wtr_ln'),
    url(r'^s_wtr_ln_dl/', views.s_wtr_ln_view_dl, name = 'rcbc_s_wtr_ln_dl'),
    url(r'^watersheds/', views.watersheds_view, name = 'rcbc_watersheds'),
    url(r'^watersheds_dl/', views.watersheds_view_dl, name = 'rcbc_watersheds_dl'),
    url(r'^document/', views.document_view, name = 'rcbc_document'),
    url(r'^document_dl/', views.document_view_dl, name = 'rcbc_document_dl'),

]
