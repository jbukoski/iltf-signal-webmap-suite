from comanche.models import counties, cotton, caddo
from django.conf.urls import url
from djgeojson.views import GeoJSONLayerView
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^counties/', GeoJSONLayerView.as_view(model=counties), name='counties'),
    url(r'^cotton/', GeoJSONLayerView.as_view(model=cotton), name='cotton'),
    url(r'^caddo/', GeoJSONLayerView.as_view(model=caddo), name='caddo'),
]
