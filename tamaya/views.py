from django.conf import settings
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import boundary, mbls, roads, soil_data, user_pts, user_lines, user_polygons
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import json
import os

from django.template import RequestContext
from django.urls import reverse
from .forms import Document, DocumentForm

def list(request):
    # Handles file upload

    print("\nCheck in list view function....\n")

    print("\n===========")
    print("list request: ", request)
    print("list request.FILES: ", request.FILES)
    print("===========\n")

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('tamaya.views.list'))
    else:
        form = DocumentForm()       # Empty

    # Load documents from the list page
    documents = Document.objects.all()

    # Render list page with all documents
    """return render_to_response(
        'tamaya/list.html',
        {
            'documents' : documents,
            'form' : form
        },
        context_instance=RequestContext(request)
    )"""
    context = {'documents' : documents, 'form' : form}
    return render(request, 'tamaya/list.html', context)

# Specify downloads path
path = os.path.dirname(os.path.abspath(__file__))

raw_json = open(os.path.join(os.path.dirname(path), 'media/tamaya/uploaded/boundary.geojson'), 'r+').read()
#load_json = json.load(raw_json)
#load_json = json.dumps(raw_json)
#print("\n\nload_json: ", load_json, "\n\n")
#raw_json.close()

@login_required(login_url='/login/')
def index(request):

    print("\n\nTHIS IS IN INDEX()\n\n")

    #print("\n\nIn index - load_json: ", load_json, "\n\n")

    bndry = boundary.objects.all()
    return render(request, 'tamaya/index.html', {
        'title': 'Santa Ana Pueblo of NM',
        'bndry': bndry,
        #'samplejson': load_json
    })

def home(request):
    return HttpResponseRedirect(urlresolvers.reverse('admin:app_list', args=("tamaya/",)))

def render_geojson_view(request):
    return HttpResponse(raw_json, content_type='json')

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

def user_lines_view(request):
    user_lines_json = serialize('geojson', user_lines.objects.all(), geometry_field="geom", fields=('name', 'comment'))
    return HttpResponse(user_lines_json, content_type='json')

def user_polygons_view(request):
    user_polygons_json = serialize('geojson', user_polygons.objects.all(), geometry_field="geom", fields=('name', 'comment'))
    return HttpResponse(user_polygons_json, content_type='json')

###############
## Downloads ##
###############

# Admin layers

def boundary_dl_view(request):
    download_file = open(os.path.join(path, 'downloads', 'boundary.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="boundary.zip"'

    return response

def mbl_dl_view(request):
    download_file = open(os.path.join(path, 'downloads', 'mbl_int.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="mbl_int.zip"'

    return response

def roads_dl_view(request):
    download_file = open(os.path.join(path, 'downloads', 'santa_ana_roads.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="reservation_roads.zip"'

    return response

# Soi layers

def bd_dl_view(request):
    download_file = open(os.path.join(path, 'downloads', 'bulk_density_1_3_bar.zip'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="bulk_density_1_3_bar.zip"'

    return response

def compost_dl_view(request):
    download_file = open(os.path.join(path, 'downloads', 'composting_medium_and_final_cover.zip'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="composting_medium_and_final_cover.zip"'

    return response

def om_dl_view(request):
    download_file = open(os.path.join(path, 'downloads', 'organic_matter.zip'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="organic_matter.zip"'

    return response

def ph_dl_view(request):
    download_file = open(os.path.join(path, 'downloads', 'ph_surface_weighted_average.zip'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="ph_surface_weighted_average.zip"'

    return response

def taxonomy_dl_view(request):
    download_file = open(os.path.join(path, 'downloads', 'soil_taxonomy.zip'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="soil_taxonomy.zip"'

    return response

def texture_dl_view(request):
    download_file = open(os.path.join(path, 'downloads', 'soil_texture_dcp.zip'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="soil_texture_dcp.zip"'

    return response

######################
## Import Utilities ##
######################

def sample_dl_view(request):
    #download_file = open(os.path.join(path, 'downloads', 'sample.zip'), "rb")
    download_file = open(os.path.join(os.path.dirname(path), 'media/tamaya/uploaded/boundary.geojson'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="boundary.geojson"'

    return response

def sample_up_view(request):

    if request.method == 'GET':

        print("\nThis is a GET event...\n")
        form = DocumentForm()

    elif request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        print("\nWithin request.method == POST...\n")

        if form.is_valid():

            filenamee = request.FILES['docfile']
            print("\n\nfilenamee: ", filenamee, "\n\n")

            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            #return HttpResponseRedirect(reverse(newdoc.url))
            return HttpResponseRedirect(reverse('sample_up'))
            #return HttpResponseRedirect(reverse('index'))

            #return render_to_response('tamaya/index.html', locals())

        else:

            print("\nForm is NOT VALID...\n")

            documents = "No Document"
            context = {'documents' : documents, 'form' : form}

            #newdoc = Document(docfile = request.FILES['docfile'])
            #newdoc.save()

            return render(request, 'tamaya/index.html', context)

    else:
        form = DocumentForm()       # Empty


    # Render list page with all documents
    #return render (
    #    request,
    #    'tamaya/',
    #    {'documents' : documents, 'form' : form}
    #)

    #download_file = open(os.path.join(path, 'downloads', 'sample.zip'), "rb")
    #response = HttpResponse(download_file, content_type='application/force-download')
    #response['Content-Disposition'] = 'attachment; filename="sample.zip"'

    #return response

    # Load documents from the list page
    documents = Document.objects.all()

    # Render list page with all documents
    """return render_to_response(
        'tamaya/list.html',
        {
            'documents' : documents,
            'form' : form
        },
        context_instance=RequestContext(request)
    )"""
    context = {'documents' : documents, 'form' : form}
    return render(request, 'tamaya/index.html', context)
