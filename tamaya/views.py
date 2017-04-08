from django.conf import settings
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import boundary, mbls, roads, soil_data, user_pts, user_lines, user_polygons
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import json
import os

@login_required(login_url='/login/')
def index(request):
    bndry = boundary.objects.all()
    return render(request, 'tamaya/index.html', {
        'title': 'Santa Ana Pueblo of NM',
        'bndry': bndry,
    })

def home(request):
    return HttpResponseRedirect(urlresolvers.reverse('admin:app_list', args=("tamaya/",)))

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

# Specify downloads path
path = os.path.dirname(os.path.abspath(__file__))

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
    download_file = open(os.path.join(path, 'downloads', 'sample.zip'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="sample.zip"'

    return response

def sample_up_view(request):

    print("\nCheck in sample upload view function....\n")

    print("\n===========")
    print("request: ", request)
    print("request.FILES: ", request.FILES)
    print("===========\n")

    if request.method == "POST":

        print("\nWithin request.method == POST...\n")

        """
        if len(request.files) > 0:

            print("\nRequest.file detected...\n")
            fileStruct = request.files['fileInput']

            # check if the post request has the file part
            if 'fileInput' not in request.files:
                print("\nNo file part\n")
                #return redirect(request.url)

            # if user does not select file, browser also
            # submit a empty part without filename
            if fileStruct.filename == '':
                print("\nNo selected file\n")
                #return redirect(request.url)

            if fileStruct.filename:

                print("\n--------------")
                print("...File upload is valid filename and structure...")
                print("--------------\n")


                filename = secure_filename(fileStruct.filename)
                fileStruct.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                # Add Bib file to relative path
                absPathh = os.path.abspath(UPLOAD_FOLDER + filename)
                bibDB = bib_parse(absPathh)

                if "collectName" in request.form:
                    if (request.form["collectName"] == '') or (len(request.form["collectName"]) == 0):
                        collectName = "Default"
                    else:
                        collectName = request.form["collectName"]
                else:
                    collectName = "Default"


                # Create table and pass in collection name
                create_table(collectName, bibDB)

                return render_template("showresults.html", collectName = collectName, filenamee = filename, fileUpload = bibDB[0], fileSize = len(bibDB))
                """

    download_file = open(os.path.join(path, 'downloads', 'sample.zip'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="sample.zip"'

    return response
