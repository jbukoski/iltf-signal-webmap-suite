from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import counties, cotton, caddo

def index(request):
    return render(request, 'comanche/index.html', {
        'title': 'Comanche',
    })

def counties_view(request):
    counties_json = serialize('geojson', counties.objects.all(), geometry_field="geom", fields=('name','pop2010','sqmi'))
    return HttpResponse(counties_json, content_type='json')

def caddo_view(request):
    caddo_json = serialize('geojson', caddo.objects.all(), geometry_field="geom", fields=('parcel_id','shape_area'))
    return HttpResponse(caddo_json, content_type='json')

def cotton_view(request):
    cotton_json = serialize('geojson', cotton.objects.all(), geometry_field="geom", fields=('parcelid','acres'))
    return HttpResponse(cotton_json, content_type='json')
