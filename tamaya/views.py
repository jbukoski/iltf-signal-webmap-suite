from django.conf import settings
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from . import models
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import json
import os, os.path
import psycopg2
import time

from django.template import RequestContext
from django.urls import reverse
from .forms import DocumentForm

from django.core.files.storage import FileSystemStorage

# Specify downloads path
path = os.path.dirname(os.path.abspath(__file__))

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

def render_geojson_view(request):

    if request.method == 'POST':
        lyr = request.POST['layer']

        lyr_json = open(os.path.join(os.path.dirname(path), 'media', lyr), 'r+').read()

        print("\n\n++++++++++++\nWithin render_geojson_view")
        print("lyr: ", lyr)
        print("lyr_json: ", lyr_json)
        print("++++++++++\n\n")

        return JsonResponse({'layer': lyr, 'layer_json': lyr_json})

    else:

        error_msg = 'Not a post request'

        return JsonResponse(error_msg, safe = False)

def legend_view(request):

    if request.method == 'POST':
        lat = request.POST['lat']
        lon = request.POST['lng']

        query = """WITH mypoint AS (SELECT ST_SetSRID(ST_MakePoint(%s, %s), 4326) geom),
                        evt_point AS (SELECT ST_Value(evt.rast, geom) AS value
                                      FROM mypoint AS p 
                                      CROSS JOIN tamaya_landfire_evt AS evt
                                      WHERE ST_Intersects(p.geom, evt.rast)),
                        evt_class AS (SELECT classes.label
                                      FROM tamaya_landfire_classes AS classes
                                      CROSS JOIN evt_point
                                      WHERE classes.value = evt_point.value),
                        ndvi2005 AS (SELECT ST_Value(ndvi2005.rast, geom) AS value
                                      FROM mypoint AS p
                                      CROSS JOIN tamaya_ndvi_2005 AS ndvi2005
                                      WHERE ST_Intersects(p.geom, ndvi2005.rast)),
                        ndvi2010 AS (SELECT ST_Value(ndvi2010.rast, geom) AS value
                                      FROM mypoint AS p
                                      CROSS JOIN tamaya_ndvi_2010 AS ndvi2010
                                      WHERE ST_Intersects(p.geom, ndvi2010.rast)),
                        ndvi2015 AS (SELECT ST_Value(ndvi2015.rast, geom) AS value
                                      FROM mypoint AS p
                                      CROSS JOIN tamaya_ndvi_2015 AS ndvi2015
                                      WHERE ST_Intersects(p.geom, ndvi2015.rast))
                        SELECT *
                        FROM evt_point, evt_class, ndvi2005, ndvi2010, ndvi2015; """ % (lon, lat)

        conn = psycopg2.connect("dbname='iltf' user='postgres'")
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()
        landfireEVT = int(results[0][0])
        evtClass = results[0][1]
        ndvi2005 = round(results[0][2], 4)
        ndvi2010 = round(results[0][3], 4)
        ndvi2015 = round(results[0][4], 4)
        conn.close()

        legText = {"landfireEVT": "&nbsp&nbsp<b>LANDFIRE Existing Vegetation Type: </b>" + str(evtClass) + "</br>",
                    "ndvi2005": "&nbsp&nbsp<b>Mean Annual NDVI, 2005: </b>" + str(ndvi2005) + "</br>",
                    "ndvi2010": "&nbsp&nbsp<b>Mean Annual NDVI, 2010: </b>" + str(ndvi2010) + "</br>",
                    "ndvi2015": "&nbsp&nbsp<b>Mean Annual NDVI, 2015: </b>" + str(ndvi2015) + "</br>"}

        return JsonResponse({'evtClass': evtClass, 'ndvi2005': ndvi2005,
                             'ndvi2010': ndvi2010, 'ndvi2015': ndvi2015,
                             'legText': legText})

    else:

        error_msg = 'Not a post request'

        return JsonResponse({'error', error_msg})

def sumstats_view(request):

    if request.method == 'POST':
        t0 = time.time()
        geom = request.POST['geom']

        query = """WITH poly AS (SELECT ST_SetSRID(ST_GeomFromGeoJSON('%s'), 4326) AS geom),
                       poly_eq_area AS (SELECT ST_Transform(geom, 32113) AS geom_eq_area FROM poly),
                       agc_clip AS (SELECT ST_Union(ST_Clip(agc.rast, poly.geom)) AS raster
                           FROM tamaya_forest_agc AS agc
                             CROSS JOIN poly
                             WHERE (ST_Intersects(poly.geom, agc.rast))),
                       bgc_clip AS (SELECT ST_Union(ST_Clip(bgc.rast, poly.geom)) AS raster
                           FROM tamaya_forest_bgc AS bgc
                             CROSS JOIN poly
                             WHERE (ST_Intersects(poly.geom, bgc.rast))),
                       soc_clip AS (SELECT ST_Union(ST_Clip(soc.rast, poly.geom)) AS raster
                           FROM tamaya_gssurgo_soc AS soc
                             CROSS JOIN poly
                             WHERE (ST_Intersects(poly.geom, soc.rast)))
                   SELECT (ST_SummaryStats(agc_clip.raster, true)).*,
                          (ST_SummaryStats(bgc_clip.raster, true)).*,
                          (ST_SummaryStats(soc_clip.raster, true)).*,
                           ST_Area(geom_eq_area) AS area
                   FROM agc_clip
                       CROSS JOIN bgc_clip
                       CROSS JOIN soc_clip
                       CROSS JOIN poly_eq_area;""" % (geom)

        conn = psycopg2.connect("dbname='iltf' user='postgres'")
        cur = conn.cursor()
        t1 = time.time()
        cur.execute(query)

        results = cur.fetchall()

        t2 = time.time()
     
        sumstats = results
        forestPixels = sumstats[0][0]
        area = round(sumstats[0][18]/10000, 2)
        agc_sum = round(sumstats[0][1], 2)
        agc_mean = round(sumstats[0][2], 2)
        bgc_sum = round(sumstats[0][7], 2)
        bgc_mean = round(sumstats[0][8], 2)
        soc_sum = round(sumstats[0][13], 2)
        soc_mean = round(sumstats[0][14], 2)
        totalArea = "{:,}".format(area, 2)
        agcTotal = "{:,}".format(round((agc_sum / 100 * 6.25), 2))
        agcMean = "{:,}".format(round(agc_mean / 100, 2))
        bgcTotal = "{:,}".format(round((bgc_sum / 100 * 6.25), 2))
        bgcMean = "{:,}".format(round(bgc_mean / 100, 2))
        socTotal = "{:,}".format(round((soc_sum / 100 * 0.01), 2))
        socMean = "{:,}".format(round(soc_mean / 100, 2))
        forestArea = "{:,}".format(round(forestPixels * 6.25, 2))
        conn.close()
            
        print("\n\n=======In Sumstats View=======")
        print(sumstats)
        print("Geom: ", geom)
        print("=======================\n\n")

        text = {'agc': "</br>&nbsp&nbsp<b>Carbon pool: </b> Aboveground Forest Carbon </br>" + 
                       "&nbsp&nbsp<b>Total carbon: </b>" + str(agcTotal) + " Mg C</br>" + 
                       "&nbsp&nbsp<b>Mean carbon: </b>" + str(agcMean) + " Mg C/ha</br>",
                'bgc': "</br>&nbsp&nbsp<b>Carbon pool: </b> Belowground Forest Carbon </br>" +
                       "&nbsp&nbsp<b>Total carbon: </b>" + str(bgcTotal) + " Mg C</br>" +
                       "&nbsp&nbsp<b>Mean carbon: </b>" + str(bgcMean) + " Mg C/ha</br>",
                'gssurgoSOC': "</br>&nbsp&nbsp<b>Carbon pool: </b> Soil Organic Carbon </br>" +
                       "&nbsp&nbsp<b>Total carbon: </b>" + str(socTotal) + " Mg C</br>" +
                       "&nbsp&nbsp<b>Mean carbon: </b>" + str(socMean) + " Mg C/ha</br>"}


        t3 = time.time()

        first = t1-t0
        second = t2-t1
        third = t3-t2
        print("\n\n===============")
        print("first: ", first)
        print("second: ", second)
        print("third: ", third)
        print("================\n\n")


        return JsonResponse({'forestPixels': forestPixels, 'text': text, 
                             'totalArea': totalArea, 'forestArea': forestArea})


    else:

        error_msg = 'Not a post request'

        return JsonResponse({'error', error_msg})


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

###############
## Downloads ##
###############

# Admin layers

def boundary_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'boundary.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="boundary.zip"'

    return response

def mbl_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'mbl_int.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="mbl_int.zip"'

    return response

def roads_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'santa_ana_roads.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="reservation_roads.zip"'

    return response

# Hydrology layers

def watersheds_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'watersheds.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="watersheds.zip"'

    return response

def subwatersheds_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'subwatersheds.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="subwatersheds.zip"'

    return response

def surfacehydrology_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'surfacehydrology.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="surfacehydrology.zip"'

    return response

# Soil layers

def bd_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'bulk_density_1_3_bar.zip'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="bulk_density_1_3_bar.zip"'

    return response

def compost_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'composting_medium_and_final_cover.zip'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="composting_medium_and_final_cover.zip"'

    return response

def om_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'organic_matter.zip'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="organic_matter.zip"'

    return response

def ph_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'ph_surface_weighted_average.zip'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="ph_surface_weighted_average.zip"'

    return response

def taxonomy_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'soil_taxonomy.zip'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="soil_taxonomy.zip"'

    return response

def texture_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'surface_texture_dcp.zip'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="soil_texture_dcp.zip"'

    return response

## Vegetation layers

def landfire_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'landfireEVT.tif'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="tamaya_landfire_evt.tif"'

    return response

def ndvi_2005_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'tamaya_ndvi_2005.tif'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="tamaya_ndvi_2005.tif"'

    return response

def ndvi_2010_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'tamaya_ndvi_2010.tif'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="tamaya_ndvi_2010.tif"'

    return response

def ndvi_2015_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'tamaya_ndvi_2015.tif'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="tamaya_ndvi_2015.tif"'

    return response

## Carbon layers

def agc_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'tamaya_forest_agc.tif'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="tamaya_forest_agc.tif"'

    return response

def bgc_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'tamaya_forest_bgc.tif'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="tamaya_forest_bgc.tif"'

    return response

def soc_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'tamaya_gssurgo_soc.tif'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="tamaya_gssurgo_soc.tif"'

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
