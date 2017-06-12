from django.conf import settings
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import json
import os, os.path
import psycopg2

from django.template import RequestContext
from django.urls import reverse
from .forms import DocumentForm

from django.core.files.storage import FileSystemStorage

# Specify downloads path
path = os.path.dirname(os.path.abspath(__file__))

raw_json = open(os.path.join(os.path.dirname(path), 'media/tamaya/uploaded/boundary.geojson'), 'r+').read()
#load_json = json.load(raw_json)
#load_json = json.dumps(raw_json)
#raw_json.close()

@login_required(login_url='/login/')
def index(request):

    bndry = models.boundary.objects.all()
    documents = models.Document.objects.all()
    upload_files = next(os.walk(os.path.join(os.path.dirname(path), 'media/tamaya/uploaded')))[2]
    upload_list = []

    for up_file in upload_files:

        if up_file != ".DS_Store":

            up_file_path = os.path.join(os.path.dirname(path), 'media/tamaya/uploaded/', up_file)
            raw_doc_json = open(os.path.join(os.path.dirname(path), 'media/tamaya/uploaded/', up_file)).read()
            upload_list.append(raw_doc_json)

            #print("\n=============\nWithin index upload_files")
            #print("upload_list: ", upload_list)
            #print("\n=========\n\n")

    doc_counter = 1

    for document in documents:
        doc_counter += 1

    return render(request, 'tamaya/index.html', {
        'title': 'Santa Ana Pueblo of NM',
        'bndry': bndry,
        'documents': documents
    })

def home(request):
    return HttpResponseRedirect(urlresolvers.reverse('admin:app_list', args=("tamaya/",)))

def list(request):
    # Handles file upload

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            newdoc = models.Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('tamaya.views.list'))
    else:
        form = DocumentForm()       # Empty

    # Load documents from the list page
    documents = models.Document.objects.all()

    # Render list page with all documents
    context = {'documents' : documents, 'form' : form}
    return render(request, 'tamaya/list.html', context)

def render_geojson_view(request, *args, **kwargs):

    print("\n\n++++++++++++\nWithin render_geojson_view")
    print("args: ", args)
    print("kwargs: ", kwargs)
    print("++++++++++\n\n")
    
    return HttpResponse(raw_json, content_type='json')

def legend_view(request):

    lat = request.POST['lat']
    lon = request.POST['lng']

    query = "SELECT ST_Value(raster, ST_TRANSFORM(ST_SetSRID(ST_MakePoint(%s, %s), 4326), 4326)) FROM tamaya_testraster;" % (lon, lat)

    conn = psycopg2.connect("dbname='iltf' user='postgres'")
    cur = conn.cursor() 
    cur.execute(query)
    result = "The value is %s" % cur.fetchall()[0][0]
    result_json = json.dumps(result)
    test_string = "This is a test string."

    print("\n\n++++++++++++\nInside the legend view\n")
    print("Lat: ", lat, "   Lon: ", lon)
    print("Value: ", result)
    print("++++++++++++\n\n")

    return HttpResponse(result_json, content_type='json')

def boundary_view(request):
    boundary_json = serialize('geojson', models.boundary.objects.all(), geometry_field="geom")
    return HttpResponse(boundary_json, content_type='json')

def mbls_view(request):
    mbls_json = serialize('geojson', models.mbls.objects.all(), geometry_field="geom", fields=('area', 'acres', 'comment', 'perimeter', 'mbl_field'))
    return HttpResponse(mbls_json, content_type='json')

def roads_view(request):
    roads_json = serialize('geojson', models.roads.objects.all(), geometry_field="geom", fields=('name', 'surface', 'comment', 'condition', 'id'))
    return HttpResponse(roads_json, content_type='json')

def watersheds_view(request):
    watersheds_json = serialize('geojson', models.watersheds.objects.all(), geometry_field="geom", fields=('watershed_id', 'hu_8_name', 'shape_area'))
    return HttpResponse(watersheds_json, content_type="json")

def subwatersheds_view(request):
    subwatersheds_json = serialize('geojson', models.subwatersheds.objects.all(), geometry_field="geom", fields=('subwatershed_id', 'watershed', 'subwatshed', 'acres'))
    return HttpResponse(subwatersheds_json, content_type="json")

def surfacehydro_view(request):
    surfacehydro_json = serialize('geojson', models.surfacehydro.objects.all(), geometry_field="geom")
    return HttpResponse(surfacehydro_json, content_type="json")

def soil_data_view(request):
    soil_data_json = serialize('geojson', models.soil_data.objects.all(), geometry_field="geom", fields=('poly_id','tax_class', 'org_matter', 'composting', 'texture', 'ph_water', 'bulk_densi'))
    return HttpResponse(soil_data_json, content_type='json')

def user_points_view(request):
    user_pt_json = serialize('geojson', models.user_pts.objects.all(), geometry_field="geom", fields=('name', 'comment'))
    return HttpResponse(user_pt_json, content_type='json')

def user_lines_view(request):
    user_lines_json = serialize('geojson', models.user_lines.objects.all(), geometry_field="geom", fields=('name', 'comment'))
    return HttpResponse(user_lines_json, content_type='json')

def user_polygons_view(request):
    user_polygons_json = serialize('geojson', models.user_polygons.objects.all(), geometry_field="geom", fields=('name', 'comment'))
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

# Soil layers

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

    try:
        if request.GET:

            print("request.GET: ", request.GET)

        elif request.POST:

            body_raw = request.body.decode("utf-8")
            end_file_name = len(body_raw)
            loc_file_name = body_raw.find("file_name")
            start_file_name = loc_file_name + 10        # where 'file_name=' starts + ends
            try_text_name = body_raw[start_file_name:end_file_name]
            text_name = try_text_name.replace("%2F", "/")

            if text_name == "boundary.geojson":

                download_file = open(os.path.join(os.path.dirname(path), 'media/tamaya/uploaded/boundary.geojson'), "rb")
                response = HttpResponse(download_file, content_type='application/force-download')
                response['Content-Disposition'] = 'attachment; filename="boundary.geojson"'
                return response

            else:

                all_docs = models.Document.objects.all()

                for document in all_docs:

                    foo_url = document.docfile.url
                    name_len = len(text_name)
                    short_name = text_name[16:name_len]

                    if document.docfile.name == text_name:

                        download_file = open(os.path.join(os.path.dirname(path), "media/tamaya/uploaded/", short_name), "rb")
                        response = HttpResponse(download_file, content_type='application/force-download')
                        response['Content-Disposition'] = 'attachment; filename="' + short_name + '"'
                        return response

            download_file = open(os.path.join(os.path.dirname(path), document.docfile.url), "rb")
            response = HttpResponse(download_file, content_type='application/force-download')
            response['Content-Disposition'] = 'attachment; filename="FAIL_FILE.sad"'
            return response
    except:

        print("\nError in request POST event\n")
        return HttpResponseRedirect(reverse('index'))

def sample_up_view(request):

    if request.method == 'GET':
        form = DocumentForm()

    elif request.method == 'POST':

        if request.FILES['docfile']:

            form = DocumentForm(request.POST, request.FILES)

            if form.is_valid():

                this_file = request.FILES['docfile']
                file_sys = FileSystemStorage()

                file_path = os.path.join('tamaya/uploaded/', this_file.name)
                #file_name = file_sys.save(this_file.name, this_file)
                #file_name = file_sys.save(file_path, this_file)
                #this_file_url = file_sys.url(file_name)

                #filenamee = request.FILES['docfile']
                newdoc = models.Document(docfile = request.FILES['docfile'])
                newdoc.save()

                #return HttpResponseRedirect(reverse(newdoc))
                return HttpResponseRedirect(reverse('index'))
        return render(request, 'index.html')

    else:
        form = DocumentForm()       # Empty

    # Load documents from the list page
    documents = models.Document.objects.all()
    context = {'documents' : documents, 'form' : form}

    return render(request, 'tamaya/index.html', context)

def delete_up_view(request):

    i = 0
    documents = models.Document.objects.all()
    for document in documents:

        i += 1

        print("\n\n============\nDocument: ", document)
        print("os.path.join(settings.MEDIA_ROOT, document.docfile.name): ", os.path.join(settings.MEDIA_ROOT, document.docfile.name))
        print("\n===========\n\n")

        os.remove(os.path.join(settings.MEDIA_ROOT, document.docfile.name))
        document.delete()


    return HttpResponseRedirect(reverse('index'))
