from django.conf import settings
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import json
import os, os.path

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

    print("\n\nWithin index in views...\n\n")

    bndry = models.boundary.objects.all()
    documents = models.Document.objects.all()

    upload_files = next(os.walk(os.path.join(os.path.dirname(path), 'media/tamaya/uploaded')))[2]

    for up_file in upload_files:

        if up_file != ".DS_Store":

            up_file_path = os.path.join(os.path.dirname(path), 'media/tamaya/uploaded/', up_file)

            print("\n\nWithin index views.py")
            print("up_file: ", up_file)
            print("up_file_path: ", up_file_path)
            print("---------------\n\n")
            os.path.join(os.path.dirname(path), 'media/tamaya/uploaded/', up_file)

    foo_counter = 1

    for document in documents:
        print("\n\nWithin index views.py...")
        print("counter: ", foo_counter)
        foo_counter += 1
        print("document: ", document)
        #print("document.value: ", document.value)
        print("document.docfile: ", document.docfile)
        print("==================\n\n")

    print("\n\nWithin index views.py")
    print("upload_files: ", upload_files)
    print("len(upload_files): ", len(upload_files))
    print("---------------\n\n")

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

def render_geojson_view(request):
    return HttpResponse(raw_json, content_type='json')

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
    watersheds_json = serialize('geojson', models.watersheds.objects.all(), geometry_field="geom")
    return HttpResponse(watersheds_json, content_type="json")

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

    print("\n\nWithin sample_dl_view")

    try:
        if request.GET:

            print("request.GET: ", request.GET)

        elif request.POST:

            body_raw = request.body.decode("utf-8")
            end_file_name = len(body_raw)
            loc_file_name = body_raw.find("file_name")
            start_file_name = loc_file_name + 10        # where 'file_name=' starts + ends
            text_name = body_raw[start_file_name:end_file_name]

            if text_name == "boundary.geojson":

                print("\nTEXT_NAME is boundary.geojson...")
                print("======================\n\n")

                download_file = open(os.path.join(os.path.dirname(path), 'media/tamaya/uploaded/boundary.geojson'), "rb")
                response = HttpResponse(download_file, content_type='application/force-download')
                response['Content-Disposition'] = 'attachment; filename="boundary.geojson"'
                return response

            else:

                all_docs = models.Document.objects.all()

                #print("document.docfile.url: ", document.docfile.url)

                print("\nall_docs: ", all_docs)

                for document in all_docs:
                    print("document.docfile.url: ", document.docfile.url)


                print("\n+_+_++_+_+_++ in Else statement...\n\n")
                print("text_name: ", text_name)
                print("------\n\n")

                download_file = open(os.path.join(os.path.dirname(path), 'media/tamaya/uploaded/boundary.geojson'), "rb")
                response = HttpResponse(download_file, content_type='application/force-download')
                response['Content-Disposition'] = 'attachment; filename="boundary.geojson"'
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

                print("\n\nIn sample_up_view")
                print("request.FILES['docfile']: ", request.FILES['docfile'])
                print("this_file.name: ", this_file.name)
                print("file_path: ", file_path)
                #print("newdoc: ", newdoc)
                #print("newdoc.value: ", newdoc.value)
                print("----------------\n\n")

                #return render(request, 'index.html', {
                #    'this_file_url' : this_file_url
                #})

                #return HttpResponseRedirect(reverse(newdoc))
                return HttpResponseRedirect(reverse('index'))

            # Redirect to the document list after POST
            #return HttpResponseRedirect(reverse(newdoc.url))
            #return HttpResponseRedirect(reverse('sample_up'))
            #return HttpResponseRedirect(reverse('index'))
            #next = request.POST.get('docfile', '/tamaya')
            #return HttpResponseRedirect(next)

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
        print("--\ni: ", i)
        print("document: ", document)
        #print("document.docfile.url: ", document.docfile.url)

        document.delete()

    #next = request.POST.get('del_files', '/tamaya')
    #return HttpResponseRedirect(next)
    return HttpResponseRedirect(reverse('index'))
