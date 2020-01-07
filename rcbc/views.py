from django.conf import settings
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from . import models
from django.core.serializers import serialize
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import json, os, os.path, psycopg2, re, time

from django.template import RequestContext
from django.urls import reverse
from .forms import DocumentForm

from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError

# Specify downloads path
path = os.path.dirname(os.path.abspath(__file__))

@login_required(login_url='/login/')
def index(request):
     
    if not request.user.username == 'rcbc_user':
        return HttpResponseRedirect(reverse('iltf_index'))

    bndry = models.boundary.objects.all()
    documents = models.Document.objects.all()
    upload_files = next(os.walk(os.path.join(os.path.dirname(path), 'media/rcbc/uploaded')))[2]
    upload_list = []

    for up_file in upload_files:

        if up_file != ".DS_Store":

            up_file_path = os.path.join(os.path.dirname(path), 'media/rcbc/uploaded/', up_file)
            raw_doc_json = open(os.path.join(os.path.dirname(path), 'media/rcbc/uploaded/', up_file)).read()
            upload_list.append(raw_doc_json)

    doc_counter = 1

    for document in documents:
        doc_counter += 1

    return render(request, 'rcbc/index.html', {
        'title': 'Red Cliff Band of the Lake Superior Chippewa',
        'bndry': bndry,
        'documents': documents
    })

def home(request):
    return HttpResponseRedirect(urlresolvers.reverse('admin:app_list', args=("rcbc/",)))

def render_geojson_view(request):

    if request.method == 'POST':
        lyr = request.POST['layer']
        lyr_json = open(os.path.join(os.path.dirname(path), 'media', lyr), 'r+').read()

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
                                      CROSS JOIN rcbc_landfire_evt AS evt
                                      WHERE ST_Intersects(p.geom, evt.rast)),
                        evt_class AS (SELECT classes.label
                                      FROM rcbc_landfire_classes AS classes
                                      CROSS JOIN evt_point
                                      WHERE classes.value = evt_point.value),
                        ndvi2005 AS (SELECT ST_Value(ndvi2005.rast, geom) AS value
                                      FROM mypoint AS p
                                      CROSS JOIN rcbc_ndvi_2005 AS ndvi2005
                                      WHERE ST_Intersects(p.geom, ndvi2005.rast)),
                        ndvi2010 AS (SELECT ST_Value(ndvi2010.rast, geom) AS value
                                      FROM mypoint AS p
                                      CROSS JOIN rcbc_ndvi_2010 AS ndvi2010
                                      WHERE ST_Intersects(p.geom, ndvi2010.rast)),
                        ndvi2015 AS (SELECT ST_Value(ndvi2015.rast, geom) AS value
                                      FROM mypoint AS p
                                      CROSS JOIN rcbc_ndvi_2015 AS ndvi2015
                                      WHERE ST_Intersects(p.geom, ndvi2015.rast)),
                        agc AS (SELECT ST_Value(agc.rast, geom) AS value
                                      FROM mypoint AS p
                                      CROSS JOIN rcbc_forest_agc AS agc
                                      WHERE ST_Intersects(p.geom, agc.rast)),
                        bgc AS (SELECT ST_Value(bgc.rast, geom) AS value
                                      FROM mypoint AS p
                                      CROSS JOIN rcbc_forest_bgc AS bgc
                                      WHERE ST_Intersects(p.geom, bgc.rast)),
                        soc AS (SELECT ST_Value(soc.rast, geom) AS value
                                      FROM mypoint AS p
                                      CROSS JOIN rcbc_gssurgo_soc AS soc
                                      WHERE ST_Intersects(p.geom, soc.rast))
                        SELECT *
                        FROM evt_point, evt_class, ndvi2005, ndvi2010, ndvi2015, agc, bgc, soc; """ % (lon, lat)

        conn = psycopg2.connect("dbname='iltf' user='postgres'")
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()

        landfireEVT = int(results[0][0])
        evtClass = results[0][1]
        ndvi2005 = round(results[0][2], 4)
        ndvi2010 = round(results[0][3], 4)
        ndvi2015 = round(results[0][4], 4)
        if results[0][5] is None:
            agc = 'No forest present'
            bgc = 'No forest present'
        else:
                agc = str(round(results[0][5] / 100, 4)) + " Mg/ha"
                bgc = str(round(results[0][6] / 100, 4)) + " Mg/ha"
        soc = round(results[0][7] / 100, 4)
        conn.close()

        legText = {"landfireEVT": "&nbsp&nbsp<b>LANDFIRE EVT: </b>" + str(evtClass) + "</br>",
                    "ndvi2005": "&nbsp&nbsp<b>Mean Annual NDVI, 2005: </b>" + str(ndvi2005) + "</br>",
                    "ndvi2010": "&nbsp&nbsp<b>Mean Annual NDVI, 2010: </b>" + str(ndvi2010) + "</br>",
                    "ndvi2015": "&nbsp&nbsp<b>Mean Annual NDVI, 2015: </b>" + str(ndvi2015) + "</br>",
                    "agc": "&nbsp&nbsp<b>Aboveground forest carbon: </b>" + str(agc) + "</br>",
                    "bgc": "&nbsp&nbsp<b>Belowground forest carbon: </b>" + str(bgc) + "</br>",
                    "gssurgoSOC": "&nbsp&nbsp<b>Soil organic carbon: </b>" + str(soc) + "&nbsp;Mg/ha</br>"}

        print("/n/n", legText, "/n/n")

        return JsonResponse({'evtClass': evtClass, 'ndvi2005': ndvi2005,
                             'ndvi2010': ndvi2010, 'ndvi2015': ndvi2015,
                             'legText': legText})

    else:

        error_msg = 'Not a post request'

        return JsonResponse({'error', error_msg})

def sumstats_view(request):

    if request.method == 'POST':
        geom = request.POST['geom']

        query = """WITH poly AS (SELECT ST_SetSRID(ST_GeomFromGeoJSON('%s'), 4326) AS geom),
                       poly_eq_area AS (SELECT ST_Transform(geom, 32113) AS geom_eq_area FROM poly),
                       agc_clip AS (SELECT ST_Union(ST_Clip(agc.rast, poly.geom)) AS raster
                           FROM rcbc_forest_agc AS agc
                             CROSS JOIN poly
                             WHERE (ST_Intersects(poly.geom, agc.rast))),
                       bgc_clip AS (SELECT ST_Union(ST_Clip(bgc.rast, poly.geom)) AS raster
                           FROM rcbc_forest_bgc AS bgc
                             CROSS JOIN poly
                             WHERE (ST_Intersects(poly.geom, bgc.rast))),
                       soc_clip AS (SELECT ST_Union(ST_Clip(soc.rast, poly.geom)) AS raster
                           FROM rcbc_gssurgo_soc AS soc
                             CROSS JOIN poly
                             WHERE (ST_Intersects(poly.geom, soc.rast)))
                   SELECT ST_Area(geom_eq_area) AS area,
                         (ST_SummaryStats(agc_clip.raster, true)).*,
                         (ST_SummaryStats(bgc_clip.raster, true)).*,
                         (ST_SummaryStats(soc_clip.raster, true)).*
                   FROM poly_eq_area
                       CROSS JOIN agc_clip
                       CROSS JOIN bgc_clip
                       CROSS JOIN soc_clip;""" % (geom)

        conn = psycopg2.connect("dbname='iltf' user='postgres'")
        cur = conn.cursor()
        cur.execute(query)

        results = cur.fetchall()

        sumstats = [i for i in results[0]]

        for i in range(len(sumstats)):
            if(sumstats[i] is None):
                sumstats[i] = 0
            else: 
                sumstats[i] = round(sumstats[i], 2)

        forestPixels = sumstats[1]
        area = sumstats[0]/10000
        totalArea = "{:,}".format(round(area, 2))
        forestArea = "{:,}".format(round(forestPixels * 6.25, 2))
        agc_sum = sumstats[2]
        agc_mean = sumstats[3]
        bgc_sum = sumstats[8]
        bgc_mean = sumstats[9]
        soc_sum = sumstats[14]
        soc_mean = sumstats[15]
        agcTotal = "{:,}".format(round((agc_sum / 100 * 6.25), 2))
        agcMean = "{:,}".format(round(agc_mean / 100, 2))
        bgcTotal = "{:,}".format(round((bgc_sum / 100 * 6.25), 2))
        bgcMean = "{:,}".format(round(bgc_mean / 100, 2))
        socTotal = "{:,}".format(round((soc_sum / 100 * 0.01), 2))
        socMean = "{:,}".format(round(soc_mean / 100, 2))
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

        return JsonResponse({'forestPixels': forestPixels, 'text': text, 
                             'totalArea': totalArea, 'forestArea': forestArea})

    else:

        error_msg = 'Not a post request'

        return JsonResponse({'error', error_msg})


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

                download_file = open(os.path.join(os.path.dirname(path), 'media/rcbc/uploaded/boundary.geojson'), "rb")
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

                        download_file = open(os.path.join(os.path.dirname(path), "media/rcbc/uploaded/", short_name), "rb")
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

                file_path = os.path.join('rcbc/uploaded/', this_file.name)

                filename = re.sub('\.geojson$', '', this_file.name)

                newdoc = models.Document(docfile = request.FILES['docfile'], name=filename)
                newdoc.save()

                documents = models.Document.objects.all()

                return HttpResponseRedirect(reverse('rcbc_index'))

        return render(request, 'rcbc_index')

    else:
        form = DocumentForm()       # Empty

    # Load documents from the list page

    context = {'documents' : documents, 'form' : form}

    return render(request, 'rcbc_index', context)

def download_single_view(request):

    if request.method == "POST":

        file2download = request.POST['dl_file']

        download_file = open(os.path.join(os.path.dirname(path), 'media', file2download), "rb")
        response = HttpResponse(download_file, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename="user_download.geojson"'

        return response

def delete_single_view(request):

    if request.method == "POST":

        file2delete = request.POST['dat']

        os.remove(os.path.join(settings.MEDIA_ROOT, file2delete))

        documents = models.Document.objects.all()
        doc2delete = documents.filter(docfile=file2delete)
        doc2delete.delete()

        return HttpResponseRedirect(reverse('rcbc_index'))


def delete_up_view(request):

    i = 0
    documents = models.Document.objects.all()
    for document in documents:

        i += 1

        os.remove(os.path.join(settings.MEDIA_ROOT, document.docfile.name))
        document.delete()

    return HttpResponseRedirect(reverse('rcbc_index'))

# Logout

def signout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('iltf_index'))

## Layer Views

def s_wtr_ln_view(request):
    s_wtr_ln_json = serialize('geojson', models.s_wtr_ln.objects.all(), geometry_field='geom', fields = ('dfirm_id', 'version_id', 'wtr_ln_id', 'wtr_nm', 'shown_firm', 'shown_indx', 'source_cit', 'geom', 'id'))
    return HttpResponse(s_wtr_ln_json, content_type='json')

def ashland_cnty_view(request):
    ashland_cnty_json = serialize('geojson', models.ashland_cnty.objects.all(), geometry_field='geom', fields = ('objectid', 'name', 'state_name', 'state_fips', 'cnty_fips', 'fips', 'population', 'pop_sqmi', 'pop2010', 'pop10_sqmi', 'white', 'black', 'ameri_es', 'asian', 'hawn_pi', 'hispanic', 'other', 'mult_race', 'males', 'females', 'age_under5', 'age_5_9', 'age_10_14', 'age_15_19', 'age_20_24', 'age_25_34', 'age_35_44', 'age_45_54', 'age_55_64', 'age_65_74', 'age_75_84', 'age_85_up', 'med_age', 'med_age_m', 'med_age_f', 'households', 'ave_hh_sz', 'hsehld_1_m', 'hsehld_1_f', 'marhh_chd', 'marhh_no_c', 'mhh_child', 'fhh_child', 'families', 'ave_fam_sz', 'hse_units', 'vacant', 'owner_occ', 'renter_occ', 'no_farms12', 'ave_size12', 'crop_acr12', 'ave_sale12', 'sqmi', 'shape_leng', 'shape_area', 'geom', 'id'))
    return HttpResponse(ashland_cnty_json, content_type='json')

def fbtnp_view(request):
    fbtnp_json = serialize('geojson', models.fbtnp.objects.all(), geometry_field='geom', fields = ('geom', 'id'))
    return HttpResponse(fbtnp_json, content_type='json')

def s_fld_haz_ln_view(request):
    s_fld_haz_ln_json = serialize('geojson', models.s_fld_haz_ln.objects.all(), geometry_field='geom', fields = ('dfirm_id', 'version_id', 'fld_ln_id', 'ln_typ', 'source_cit', 'geom', 'id'))
    return HttpResponse(s_fld_haz_ln_json, content_type='json')

def rc_zoning_districts_view(request):
    rc_zoning_districts_json = serialize('geojson', models.rc_zoning_districts.objects.all(), geometry_field='geom', fields = ('objectid', 'area', 'rbd4_field', 'rbd4_id', 'rbd4_name', 'district', 'shape_leng', 'shape_area', 'geom', 'id'))
    return HttpResponse(rc_zoning_districts_json, content_type='json')

def boundary_view(request):
    boundary_json = serialize('geojson', models.boundary.objects.all(), geometry_field='geom', fields = ('dfirm_id', 'version_id', 'pol_ar_id', 'pol_name1', 'pol_name2', 'pol_name3', 'co_fips', 'st_fips', 'comm_no', 'cid', 'ani_tf', 'ani_firm', 'com_nfo_id', 'source_cit', 'geom', 'id'))
    return HttpResponse(boundary_json, content_type='json')

def buff_bndry_view(request):
    buff_bndry_json = serialize('geojson', models.buff_bndry.objects.all(), geometry_field='geom', fields = ('geom', 'id'))
    return HttpResponse(buff_bndry_json, content_type='json')

def beachroute_view(request):
    beachroute_json = serialize('geojson', models.beachroute.objects.all(), geometry_field='geom', fields = ('state_fips', 'county_fip', 'road_name', 'route_type', 'tiger_feat', 'shape_len', 'geom', 'id'))
    return HttpResponse(beachroute_json, content_type='json')

def conservationmgmtarea_view(request):
    conservationmgmtarea_json = serialize('geojson', models.conservationmgmtarea.objects.all(), geometry_field='geom', fields = ('geom', 'id'))
    return HttpResponse(conservationmgmtarea_json, content_type='json')

def s_trnsport_ln_view(request):
    s_trnsport_ln_json = serialize('geojson', models.s_trnsport_ln.objects.all(), geometry_field='geom', fields = ('dfirm_id', 'version_id', 'trans_id', 'mtfcc', 'fullname', 'altname1', 'altname2', 'routenum', 'route_typ', 'source_cit', 'geom', 'id'))
    return HttpResponse(s_trnsport_ln_json, content_type='json')

def bayfield_cnty_view(request):
    bayfield_cnty_json = serialize('geojson', models.bayfield_cnty.objects.all(), geometry_field='geom', fields = ('objectid', 'name', 'state_name', 'state_fips', 'cnty_fips', 'fips', 'population', 'pop_sqmi', 'pop2010', 'pop10_sqmi', 'white', 'black', 'ameri_es', 'asian', 'hawn_pi', 'hispanic', 'other', 'mult_race', 'males', 'females', 'age_under5', 'age_5_9', 'age_10_14', 'age_15_19', 'age_20_24', 'age_25_34', 'age_35_44', 'age_45_54', 'age_55_64', 'age_65_74', 'age_75_84', 'age_85_up', 'med_age', 'med_age_m', 'med_age_f', 'households', 'ave_hh_sz', 'hsehld_1_m', 'hsehld_1_f', 'marhh_chd', 'marhh_no_c', 'mhh_child', 'fhh_child', 'families', 'ave_fam_sz', 'hse_units', 'vacant', 'owner_occ', 'renter_occ', 'no_farms12', 'ave_size12', 'crop_acr12', 'ave_sale12', 'sqmi', 'shape_leng', 'shape_area', 'geom', 'id'))
    return HttpResponse(bayfield_cnty_json, content_type='json')

def document_view(request):
    document_json = serialize('geojson', models.document.objects.all(), geometry_field='geom', fields = ('id', 'name', 'docfile'))
    return HttpResponse(document_json, content_type='json')

def frog_bay_trails_view(request):
    frog_bay_trails_json = serialize('geojson', models.frog_bay_trails.objects.all(), geometry_field='geom', fields = ('length', 'name', 'geom', 'id'))
    return HttpResponse(frogbaytrails_json, content_type='json')

def easyroute_view(request):
    easyroute_json = serialize('geojson', models.easyroute.objects.all(), geometry_field='geom', fields = ('state_fips', 'county_fip', 'road_name', 'route_type', 'tiger_feat', 'shape_len', 'geom', 'id'))
    return HttpResponse(easyroute_json, content_type='json')

def s_wtr_ar_view(request):
    s_wtr_ar_json = serialize('geojson', models.s_wtr_ar.objects.all(), geometry_field='geom', fields = ('dfirm_id', 'version_id', 'wtr_ar_id', 'wtr_nm', 'shown_firm', 'shown_indx', 'source_cit', 'geom', 'id'))
    return HttpResponse(s_wtr_ar_json, content_type='json')

def s_fld_haz_ar_view(request):
    s_fld_haz_ar_json = serialize('geojson', models.s_fld_haz_ar.objects.all(), geometry_field='geom', fields = ('dfirm_id', 'version_id', 'fld_ar_id', 'study_typ', 'fld_zone', 'zone_subty', 'sfha_tf', 'static_bfe', 'v_datum', 'depth', 'len_unit', 'velocity', 'vel_unit', 'ar_revert', 'ar_subtrv', 'bfe_revert', 'dep_revert', 'dual_zone', 'source_cit', 'geom', 'id'))
    return HttpResponse(s_fld_haz_ar_json, content_type='json')

def watersheds_view(request):
    watersheds_json = serialize('geojson', models.watersheds.objects.all(), geometry_field='geom', fields = ('objectid', 'shape_leng', 'shape_area', 'acres', 'avg_slope', 'watershed', 'geom', 'id'))
    return HttpResponse(watersheds_json, content_type='json')

def claytoncreektrail_view(request):
    claytoncreektrail_json = serialize('geojson', models.claytoncreektrail.objects.all(), geometry_field='geom', fields = ('type', 'tident', 'ident', 'latitude', 'longitude', 'y_proj', 'x_proj', 'comment', 'new_trk', 'new_seg', 'display', 'color', 'altitude', 'depth', 'temp', 'time', 'model', 'filename', 'ltime', 'desc_field', 'link', 'geom', 'id'))
    return HttpResponse(claytoncreektrail_json, content_type='json')

## Layer Download Views

def s_wtr_ln_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 's_wtr_ln.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="s_wtr_ln.zip"'

    return response
  
def ashland_cnty_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 'ashland_cnty.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="ashland_cnty.zip"'

    return response
  
def fbtnp_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 'fbtnp.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="fbtnp.zip"'

    return response
  
def s_fld_haz_ln_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 's_fld_haz_ln.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="s_fld_haz_ln.zip"'

    return response
  
def boundary_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 'boundary.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="boundary.zip"'

    return response
  
def buff_bndry_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 'buff_bndry.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="buff_bndry.zip"'

    return response
  
def conservationmgmtarea_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 'conservationmgmtarea.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="conservationmgmtarea.zip"'

    return response
  
def s_trnsport_ln_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 's_trnsport_ln.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="s_trnsport_ln.zip"'

    return response
  
def bayfield_cnty_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 'bayfield_cnty.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="bayfield_cnty.zip"'

    return response
  
def document_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 'document.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="document.zip"'

    return response
  
def frog_bay_trails_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 'frog_bay_trails.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="frog_bay_trails.zip"'

    return response
  
def s_wtr_ar_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 's_wtr_ar.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="s_wtr_ar.zip"'

    return response
  
def s_fld_haz_ar_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 's_fld_haz_ar.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="s_fld_haz_ar.zip"'

    return response
  
def watersheds_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 'watersheds.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="watersheds.zip"'

    return response
  
def claytoncreektrail_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 'claytoncreektrail.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="claytoncreektrail.zip"'

    return response
  
## Raster download links

## Vegetation

def rcbc_landfire_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 'rcbc_landfire_evt.tif'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="rcbc_evt.tif"'

    return response

def rcbc_ndvi_2005_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 'rcbc_ndvi_2005.tif'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="rcbc_ndvi_2005.tif"'

    return response

def rcbc_ndvi_2010_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 'rcbc_ndvi_2010.tif'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="rcbc_ndvi_2010.tif"'

    return response

def rcbc_ndvi_2015_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 'rcbc_ndvi_2015.tif'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="rcbc_ndvi_2015.tif"'

    return response


## Carbon

def rcbc_agc_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 'rcbc_agc.tif'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="rcbc_agc.tif"'

    return response

def rcbc_bgc_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 'rcbc_bgc.tif'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="rcbc_bgc.tif"'

    return response

def rcbc_soc_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 'rcbc_gssurgo_soc.tif'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="rcbc_soc.tif"'

    return response



## Layer Views

def s_wtr_ln_view(request):
    s_wtr_ln_json = serialize('geojson', models.s_wtr_ln.objects.all(), geometry_field='geom', fields = ('dfirm_id', 'version_id', 'wtr_ln_id', 'wtr_nm', 'shown_firm', 'shown_indx', 'source_cit', 'geom', 'id'))
    return HttpResponse(s_wtr_ln_json, content_type='json')

def ashland_cnty_view(request):
    ashland_cnty_json = serialize('geojson', models.ashland_cnty.objects.all(), geometry_field='geom', fields = ('objectid', 'name', 'state_name', 'state_fips', 'cnty_fips', 'fips', 'population', 'pop_sqmi', 'pop2010', 'pop10_sqmi', 'white', 'black', 'ameri_es', 'asian', 'hawn_pi', 'hispanic', 'other', 'mult_race', 'males', 'females', 'age_under5', 'age_5_9', 'age_10_14', 'age_15_19', 'age_20_24', 'age_25_34', 'age_35_44', 'age_45_54', 'age_55_64', 'age_65_74', 'age_75_84', 'age_85_up', 'med_age', 'med_age_m', 'med_age_f', 'households', 'ave_hh_sz', 'hsehld_1_m', 'hsehld_1_f', 'marhh_chd', 'marhh_no_c', 'mhh_child', 'fhh_child', 'families', 'ave_fam_sz', 'hse_units', 'vacant', 'owner_occ', 'renter_occ', 'no_farms12', 'ave_size12', 'crop_acr12', 'ave_sale12', 'sqmi', 'shape_leng', 'shape_area', 'geom', 'id'))
    return HttpResponse(ashland_cnty_json, content_type='json')

def fbtnp_view(request):
    fbtnp_json = serialize('geojson', models.fbtnp.objects.all(), geometry_field='geom', fields = ('geom', 'id'))
    return HttpResponse(fbtnp_json, content_type='json')

def s_fld_haz_ln_view(request):
    s_fld_haz_ln_json = serialize('geojson', models.s_fld_haz_ln.objects.all(), geometry_field='geom', fields = ('dfirm_id', 'version_id', 'fld_ln_id', 'ln_typ', 'source_cit', 'geom', 'id'))
    return HttpResponse(s_fld_haz_ln_json, content_type='json')

def boundary_view(request):
    boundary_json = serialize('geojson', models.boundary.objects.all(), geometry_field='geom', fields = ('area', 'perimeter', 'rbd4_field', 'rbd4_id', 'rbd4_name', 'acres', 'shape_leng', 'shape_area', 'geom', 'id'))
    return HttpResponse(boundary_json, content_type='json')

def buff_bndry_view(request):
    buff_bndry_json = serialize('geojson', models.buff_bndry.objects.all(), geometry_field='geom', fields = ('geom', 'id'))
    return HttpResponse(buff_bndry_json, content_type='json')

def frog_bay_trails_view(request):
    frog_bay_trails_json = serialize('geojson', models.frog_bay_trails.objects.all(), geometry_field='geom', fields = ('state_fips', 'county_fip', 'road_name', 'route_type', 'length', 'name', 'geom', 'id'))
    return HttpResponse(frog_bay_trails_json, content_type='json')

def conservationmgmtarea_view(request):
    conservationmgmtarea_json = serialize('geojson', models.conservationmgmtarea.objects.all(), geometry_field='geom', fields = ('geom', 'id'))
    return HttpResponse(conservationmgmtarea_json, content_type='json')

def s_trnsport_ln_view(request):
    s_trnsport_ln_json = serialize('geojson', models.s_trnsport_ln.objects.all(), geometry_field='geom', fields = ('dfirm_id', 'version_id', 'trans_id', 'mtfcc', 'fullname', 'altname1', 'altname2', 'routenum', 'route_typ', 'source_cit', 'geom', 'id'))
    return HttpResponse(s_trnsport_ln_json, content_type='json')

def bayfield_cnty_view(request):
    bayfield_cnty_json = serialize('geojson', models.bayfield_cnty.objects.all(), geometry_field='geom', fields = ('objectid', 'name', 'state_name', 'state_fips', 'cnty_fips', 'fips', 'population', 'pop_sqmi', 'pop2010', 'pop10_sqmi', 'white', 'black', 'ameri_es', 'asian', 'hawn_pi', 'hispanic', 'other', 'mult_race', 'males', 'females', 'age_under5', 'age_5_9', 'age_10_14', 'age_15_19', 'age_20_24', 'age_25_34', 'age_35_44', 'age_45_54', 'age_55_64', 'age_65_74', 'age_75_84', 'age_85_up', 'med_age', 'med_age_m', 'med_age_f', 'households', 'ave_hh_sz', 'hsehld_1_m', 'hsehld_1_f', 'marhh_chd', 'marhh_no_c', 'mhh_child', 'fhh_child', 'families', 'ave_fam_sz', 'hse_units', 'vacant', 'owner_occ', 'renter_occ', 'no_farms12', 'ave_size12', 'crop_acr12', 'ave_sale12', 'sqmi', 'shape_leng', 'shape_area', 'geom', 'id'))
    return HttpResponse(bayfield_cnty_json, content_type='json')

def document_view(request):
    document_json = serialize('geojson', models.document.objects.all(), geometry_field='geom', fields = ('id', 'name', 'docfile'))
    return HttpResponse(document_json, content_type='json')

def s_wtr_ar_view(request):
    s_wtr_ar_json = serialize('geojson', models.s_wtr_ar.objects.all(), geometry_field='geom', fields = ('dfirm_id', 'version_id', 'wtr_ar_id', 'wtr_nm', 'shown_firm', 'shown_indx', 'source_cit', 'geom', 'id'))
    return HttpResponse(s_wtr_ar_json, content_type='json')

def s_fld_haz_ar_view(request):
    s_fld_haz_ar_json = serialize('geojson', models.s_fld_haz_ar.objects.all(), geometry_field='geom', fields = ('dfirm_id', 'version_id', 'fld_ar_id', 'study_typ', 'fld_zone', 'zone_subty', 'sfha_tf', 'static_bfe', 'v_datum', 'depth', 'len_unit', 'velocity', 'vel_unit', 'ar_revert', 'ar_subtrv', 'bfe_revert', 'dep_revert', 'dual_zone', 'source_cit', 'geom', 'id'))
    return HttpResponse(s_fld_haz_ar_json, content_type='json')

def watersheds_view(request):
    watersheds_json = serialize('geojson', models.watersheds.objects.all(), geometry_field='geom', fields = ('objectid', 'shape_leng', 'shape_area', 'acres', 'avg_slope', 'watershed', 'geom', 'id'))
    return HttpResponse(watersheds_json, content_type='json')

def claytoncreektrail_view(request):
    claytoncreektrail_json = serialize('geojson', models.claytoncreektrail.objects.all(), geometry_field='geom', fields = ('type', 'tident', 'ident', 'latitude', 'longitude', 'y_proj', 'x_proj', 'comment', 'new_trk', 'new_seg', 'display', 'color', 'altitude', 'depth', 'temp', 'time', 'model', 'filename', 'ltime', 'desc_field', 'link', 'geom', 'id'))
    return HttpResponse(claytoncreektrail_json, content_type='json')

## Layer Download Views

def s_wtr_ln_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 's_wtr_ln.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="s_wtr_ln.zip"'

    return response
  
def ashland_cnty_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 'ashland_cnty.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="ashland_cnty.zip"'

    return response
  
def fbtnp_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 'fbtnp.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="fbtnp.zip"'

    return response
  
def s_fld_haz_ln_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 's_fld_haz_ln.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="s_fld_haz_ln.zip"'

    return response
  
def boundary_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 'boundary.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="boundary.zip"'

    return response
  
def buff_bndry_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 'buff_bndry.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="buff_bndry.zip"'

    return response
  
def frog_bay_trails_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 'frog_bay_trails.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="frog_bay_trails.zip"'

    return response
  
def conservationmgmtarea_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 'conservationmgmtarea.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="conservationmgmtarea.zip"'

    return response
  
def s_trnsport_ln_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 's_trnsport_ln.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="s_trnsport_ln.zip"'

    return response
  
def bayfield_cnty_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 'bayfield_cnty.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="bayfield_cnty.zip"'

    return response
  
def document_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 'document.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="document.zip"'

    return response
  
def s_wtr_ar_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 's_wtr_ar.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="s_wtr_ar.zip"'

    return response
  
def s_fld_haz_ar_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 's_fld_haz_ar.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="s_fld_haz_ar.zip"'

    return response
  
def watersheds_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 'watersheds.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="watersheds.zip"'

    return response
  
def claytoncreektrail_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'rcbc', 'claytoncreektrail.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="claytoncreektrail.zip"'

    return response
  
