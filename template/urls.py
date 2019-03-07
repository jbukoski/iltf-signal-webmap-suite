from django.conf.urls import include, url
from djgeojson.views import GeoJSONLayerView
from . import views
from django.contrib.gis import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='RENAME_index'),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}),
    url(r'^boundary/', views.boundary_view, name='boundary'),
    url(r'^buff_bndry/', views.buff_boundary_view, name='buff_bndry'),
    url(r'^soil_data/', views.soil_data_view, name='soil_data'),
    url(r'^boundary_dl/', views.boundary_dl_view, name='boundary_dl'),
    url(r'^bulk_dens_dl/', views.bd_dl_view, name='bulk_dens_dl'),
    url(r'^compost_dl/', views.compost_dl_view, name='compost_dl'),
    url(r'^org_mat_dl/', views.om_dl_view, name='om_dl'),
    url(r'^ph_dl/', views.ph_dl_view, name='ph_dl'),
    url(r'^tax_cl_dl/', views.taxonomy_dl_view, name='tax_cl_dl'),
    url(r'^texture_dl/', views.texture_dl_view, name='texture_dl'),
    url(r'^landfire_dl/$', views.landfire_dl_view, name = 'landfire_dl'),
    url(r'^ndvi_2005_dl/$', views.ndvi_2005_dl_view, name = 'ndvi_2005_dl'),
    url(r'^ndvi_2010_dl/$', views.ndvi_2010_dl_view, name = 'ndvi_2010_dl'),
    url(r'^ndvi_2015_dl/$', views.ndvi_2015_dl_view, name = 'ndvi_2015_dl'),
    url(r'^agc_dl/$', views.agc_dl_view, name = 'agc_dl'),
    url(r'^bgc_dl/$', views.bgc_dl_view, name = 'bgc_dl'),
    url(r'^soc_dl/$', views.soc_dl_view, name = 'soc_dl'),
    url(r'^sample_up/', views.sample_up_view, name='sample_up'),
    url(r'^render_geojson/', views.render_geojson_view, name='render_geojson'),
    url(r'^download_single/', views.download_single_view, name="download_single"),
    url(r'^delete_single/', views.delete_single_view, name="delete_single"),
    url(r'^delete_up/', views.delete_up_view, name='delete_up'),
    url(r'^legend/', views.legend_view, name='legend'),
    url(r'^sumstats/', views.sumstats_view, name='sumstats'),
    url(r'^admin/logout/$', views.signout_view, name='signout'),
]
