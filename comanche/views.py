from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import counties, cotton, caddo
from django.core.serializers import serialize

def index(request):
    return render(request, 'comanche/index.html', {
        'title': 'Comanche',
    })

def counties_view(request):
    counties_json = serialize('counties', counties.objects.all(), counties_field="geom")
    return HttpResponse(counties_json, content_type='json')


