from django.conf.urls import include, url
from djgeojson.views import GeoJSONLayerView
from . import views
from django.contrib.gis import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='lbst_index'),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}),
    url(r'^boundary/', views.boundary_view, name='lbst_boundary'),
    url(r'^boundary_dl/', views.boundary_dl_view, name='lbst_boundary_dl'),
    url(r'^counties/', views.counties_view, name='lbst_counties'),
    url(r'^counties_dl/', views.counties_dl_view, name='lbst_counties_dl'),
    url(r'^parcels/', views.parcels_view, name='lbst_parcels'),
    url(r'^parcels_dl/', views.parcels_dl_view, name='lbst_parcels_dl'),
    url(r'^new_purchases/', views.new_purchases_view, name='lbst_new_purchases'),
    url(r'^new_purchases_dl/', views.new_purchases_dl_view, name='lbst_new_purchases_dl'),
    url(r'^food_plots/', views.food_plots_view, name='lbst_food_plots'),
    url(r'^food_plots_dl/', views.food_plots_dl_view, name='lbst_food_plots_dl'),
    url(r'^grasslands/', views.grasslands_export_view, name='lbst_grasslands_export'),
    url(r'^grasslands_export_dl/', views.grasslands_export_dl_view, name='lbst_grasslands_export_dl'),
    url(r'^habitat_leases/', views.habitat_leases_view, name='lbst_habitat_leases'),
    url(r'^habitat_leases_dl/', views.habitat_leases_dl_view, name='lbst_habitat_leases_dl'),
    url(r'^shelterbelts/', views.shelterbelts_view, name='lbst_shelterbelts'),
    url(r'^shelterbelts_dl/', views.shelterbelts_dl_view, name='lbst_shelterbelts_dl'),
    url(r'^trees_shrubs/', views.trees_shrubs_view, name='lbst_trees_shrubs'),
    url(r'^trees_shrubs_dl/', views.trees_shrubs_dl_view, name='lbst_trees_shrubs_dl'),
    url(r'^wetlands/', views.wetlands_view, name='lbst_wetlands'),
    url(r'^wetlands_dl/', views.wetlands_dl_view, name='lbst_wetlands_dl'),
    #url(r'^avoided_c/', views.avoided_c_view, name='avoided_c'),
    url(r'^sample_up/', views.sample_up_view, name='lbst_sample_up'),
    url(r'^delete_single/', views.delete_single_view, name="lbst_delete_single"),
    url(r'^delete_up/', views.delete_up_view, name='lbst_delete_up'),
    url(r'^admin/logout/$', views.signout_view, name='signout'),
]

