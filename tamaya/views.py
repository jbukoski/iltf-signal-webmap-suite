from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import boundary, mbls, roads, bulk_density
from django.core.serializers import serialize

def index(request):
    bndry = boundary.objects.all()
    return render(request, 'tamaya/index.html', {
        'title': 'Santa Ana Pueblo of NM',
        'bndry': bndry,
    })

def boundary_view(request):
    boundary_json = serialize('geojson', boundary.objects.all(), geometry_field="geom")
    return HttpResponse(boundary_json, content_type='json')

def mbls_view(request):
    mbls_json = serialize('geojson', mbls.objects.all(), geometry_field="geom")
    return HttpResponse(mbls_json, content_type='json')

def roads_view(request):
    roads_json = serialize('geojson', roads.objects.all(), geometry_field="geom")
    return HttpResponse(roads_json, content_type='json')

def bulk_density_view(request):
    bulk_density_json = serialize('geojson', bulk_density.objects.all(), geometry_field="geom")
    return HttpResponse(bulk_density_json, content_type='json')

