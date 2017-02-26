from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import counties, cotton, caddo

def index(request):
    return render(request, 'comanche/index.html', {
        'title': 'Comanche',
    })

def counties_view(request):
    counties_json = serialize('counties', counties.objects.all(), counties_field="geom")
    return HttpResponse(counties_json, content_type='json')

def caddo_view(request):
    caddo_json = serialize('caddo', caddo.objects.all(), caddo_field="geom")
    return HttpResponse(caddo_json, content_type='json')

def cotton_view(request):
    cotton_json = serialize('cotton', cotton.objects.all(), cotton_field="geom")
    return HttpResponse(cotton_json, content_type='json')
