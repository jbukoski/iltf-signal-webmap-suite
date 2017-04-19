from django.conf.urls import include, url
from djgeojson.views import GeoJSONLayerView
from . import views
from django.contrib.gis import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}),
    url(r'^boundary/', views.boundary_view, name='boundary'),
    url(r'^mbls/', views.mbls_view, name='mbls'),
    url(r'^roads/', views.roads_view, name='roads'),
    url(r'^soil_data/', views.soil_data_view, name='soil_data'),
    url(r'^user_pts/', views.user_points_view, name='user_points'),
    url(r'^user_lines/', views.user_lines_view, name='user_lines'),
    url(r'^user_polygons/', views.user_polygons_view, name='user_polygons'),
    url(r'^boundary_dl/', views.boundary_dl_view, name='boundary_dl'),
    url(r'^mbl_dl/', views.mbl_dl_view, name='mbl_dl'),
    url(r'^roads_dl/', views.roads_dl_view, name='roads_dl'),
    url(r'^bulk_dens_dl/', views.bd_dl_view, name='bulk_dens_dl'),
    url(r'^compost_dl/', views.compost_dl_view, name='compost_dl'),
    url(r'^org_mat_dl/', views.om_dl_view, name='om_dl'),
    url(r'^ph_dl/', views.ph_dl_view, name='ph_dl'),
    url(r'^tax_cl_dl/', views.taxonomy_dl_view, name='tax_cl_dl'),
    url(r'^texture_dl/', views.texture_dl_view, name='texture_dl'),
    url(r'^sample_dl/', views.sample_dl_view, name='sample_dl'),
    url(r'^sample_up/', views.sample_up_view, name='sample_up'),
    url(r'^list/$', views.list, name='list'),
    url(r'^render_geojson/', views.render_geojson_view, name='render_geojson'),
    url(r'^delete_up/', views.delete_up_view, name='delete_up'),
]
