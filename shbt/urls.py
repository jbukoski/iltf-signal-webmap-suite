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
    url(r'^boundary/', views.boundary_view, name = 'shbt_boundary'),
    url(r'^boundary_dl/', views.boundary_view_dl, name = 'shbt_boundary_dl'),
    url(r'^districts/', views.districts_view, name = 'shbt_districts'),
    url(r'^districts_dl/', views.districts_view_dl, name = 'shbt_districts_dl'),
    url(r'^ownership/', views.ownership_view, name = 'shbt_ownership'),
    url(r'^ownership_dl/', views.ownership_view_dl, name = 'shbt_ownership_dl'),
    url(r'^range_units/', views.range_units_view, name = 'shbt_range_units'),
    url(r'^range_units_dl/', views.range_units_view_dl, name = 'shbt_range_units_dl'),
    url(r'^document/', views.document_view, name = 'shbt_document'),
    url(r'^document_dl/', views.document_view_dl, name = 'shbt_document_dl'),

]
