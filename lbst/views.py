from django.conf import settings
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import lbst_boundary, lbst_parcels, lbst_new_parcels, food_plots, grasslands, habitat_leases, shelterbelts, trees_shrubs, wetlands
import json
import os

def index(request):
    return render(request, 'lbst/index.html', {
        'title': 'Lower Brule Sioux Tribe',
    })

def lbst_boundary_view(request):
    lbst_boundary_json = serialize('geojson', lbst_boundary.objects.all(), geometry_field="geom")
    return HttpResponse(lbst_boundary_json, content_type='json')

def lbst_parcels_view(request):
    lbst_parcels_json = serialize('geojson', lbst_parcels.objects.all(), geometry_field="geom")
    return HttpResponse(lbst_parcels_json, content_type='json')

def lbst_new_parcels_view(request):
    lbst_new_parcels_json = serialize('geojson', lbst_new_parcels.objects.all(), geometry_field="geom")
    return HttpResponse(lbst_new_parcels_json, content_type='json')


def food_plots_view(request):
    food_plots_json = serialize('geojson', food_plots.objects.all(), geometry_field="geom")
    return HttpResponse(food_plots_json, content_type='json')

def grasslands_view(request):
    grasslands_json = serialize('geojson', grasslands.objects.all(), geometry_field="geom")
    return HttpResponse(grasslands_json, content_type='json')

def habitat_leases_view(request):
    habitat_leases_json = serialize('geojson', habitat_leases.objects.all(), geometry_field="geom")
    return HttpResponse(habitat_leases_json, content_type='json')

def shelterbelts_view(request):
    shelterbelts_json = serialize('geojson', shelterbelts.objects.all(), geometry_field="geom")
    return HttpResponse(shelterbelts_json, content_type='json')

def trees_shrubs_view(request):
    trees_shrubs_json = serialize('geojson', trees_shrubs.objects.all(), geometry_field="geom")
    return HttpResponse(trees_shrubs_json, content_type='json')

def wetlands_view(request):
    wetlands_json = serialize('geojson', wetlands.objects.all(), geometry_field="geom")
    return HttpResponse(wetlands_json, content_type='json')
