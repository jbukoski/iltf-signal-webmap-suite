from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import boundary, mbls, roads, soil_data, user_pts
from django.core.serializers import serialize
import json

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
    mbls_json = serialize('geojson', mbls.objects.all(), geometry_field="geom", fields=('area', 'acres', 'comment', 'perimeter', 'mbl_field'))
    return HttpResponse(mbls_json, content_type='json')

def roads_view(request):
    roads_json = serialize('geojson', roads.objects.all(), geometry_field="geom", fields=('name', 'surface', 'comment', 'condition', 'id'))
    return HttpResponse(roads_json, content_type='json')

def soil_data_view(request):
    soil_data_json = serialize('geojson', soil_data.objects.all(), geometry_field="geom", fields=('poly_id','tax_class', 'org_matter', 'composting', 'texture', 'ph_water', 'bulk_densi'))
    return HttpResponse(soil_data_json, content_type='json')

def user_points_view(request):
    user_pt_json = serialize('geojson', user_pts.objects.all(), geometry_field="geom", fields=('name', 'comment'))
    return HttpResponse(user_pt_json, content_type='json')

# Downloads

#def boundary_dl(request):
#    zip_file = open(), 'r')
#    response = HttpResponse(zip_file, content_type = 'application/force-download')
#    response['Content-Disposition'] = 'attachment; filename="bulk_density_1_3_bar.zip"'
#    return response
