from django.conf.urls import include, url
from djgeojson.views import GeoJSONLayerView
from . import views
from django.contrib.gis import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='lbst_index'),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}),
    url(r'^boundary/', views.boundary_view, name='lbst_boundary'),
    #url(r'^lbst_parcels/', views.lbst_parcels_view, name='lbst_parcels'),
    #url(r'^lbst_new_parcels/', views.lbst_new_parcels_view, name='lbst_new_parcels'),
    #url(r'^food_plots/', views.food_plots_view, name='food_plots'),
    #url(r'^grasslands/', views.grasslands_view, name='grasslands'),
    #url(r'^habitat_leases/', views.habitat_leases_view, name='habitat_leases'),
    #url(r'^shelterbelts/', views.shelterbelts_view, name='shelterbelts'),
    #url(r'^trees_shrubs/', views.trees_shrubs_view, name='trees_shrubs'),
    #url(r'^wetlands/', views.wetlands_view, name='wetlands'),
    #url(r'^avoided_c/', views.avoided_c_view, name='avoided_c'),
    url(r'^admin/logout/$', views.signout_view, name='signout'),
]

