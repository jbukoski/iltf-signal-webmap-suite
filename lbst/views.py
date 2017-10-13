from django.conf import settings
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.serializers import serialize
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from . import models
import json, os, os.path, psycopg2, re, time

from django.template import RequestContext
from django.urls import reverse
from .forms import DocumentForm

from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError

#Specify downloads path
path = os.path.dirname(os.path.abspath(__file__))

@login_required(login_url='/login/')
def index(request):

    if not request.user.username == 'lbst_user':
        return HttpResponseRedirect(reverse('iltf_index'))

    return render(request, 'lbst/index.html', {
        'title': 'Lower Brule Sioux Tribe',
    })

def boundary_view(request):
    boundary_json = serialize('geojson', models.boundary.objects.all(), geometry_field="geom")
    return HttpResponse(boundary_json, content_type='json')

def signout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('iltf_index'))
