from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import boundary, mbls, roads, bulk_density, soil_ph
from django.core.serializers import serialize
import json

def index(request):
    bndry = boundary.objects.all()
    ph_json = serialize('geojson', soil_ph.objects.all(), geometry_field="geom", fields=('phwater'))
    return render(request, 'tamaya/index.html', {
        'title': 'Santa Ana Pueblo of NM',
        'bndry': bndry,
        'ph_json': ph_json,
    })

def boundary_view(request):
    boundary_json = serialize('geojson', boundary.objects.all(), geometry_field="geom")
    return HttpResponse(boundary_json, content_type='json')

def mbls_view(request):
    mbls_json = serialize('geojson', mbls.objects.all(), geometry_field="geom", fields=('area', 'acres', 'comment', 'perimeter', 'mbl_field'))
    return HttpResponse(mbls_json, content_type='json')

def roads_view(request):
    roads_json = serialize('geojson', roads.objects.all(), geometry_field="geom", fields=('name', 'surface', 'comment', 'condition', 'id'))
    return HttpResponse(roads_json, content_type='json')

def bulk_density_view(request):
    bulk_density_json = serialize('geojson', bulk_density.objects.all(), geometry_field="geom", fields=('db3rdbar'))
    return HttpResponse(bulk_density_json, content_type='json')

def soil_ph_view(request):
    soil_ph_json = serialize('geojson', soil_ph.objects.all(), geometry_field="geom", fields=('phwater'))
    return HttpResponse(soil_ph_json, content_type='json')


