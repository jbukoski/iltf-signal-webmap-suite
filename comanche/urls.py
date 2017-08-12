from comanche.models import counties, cotton, caddo
from django.conf.urls import url
from djgeojson.views import GeoJSONLayerView
from . import views

urlpatterns = [
    url(r'^$', views.index, name='comanche_index'),
    url(r'^counties/', views.counties_view, name='counties'),
    url(r'^boundaries/', views.boundaries_view, name='boundaries'),
    url(r'^cotton/', views.cotton_view, name='cotton'),
    url(r'^caddo/', views.caddo_view, name='caddo'),
]
