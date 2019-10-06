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
     
    if not request.user.username == 'bmic_user':
        return HttpResponseRedirect(reverse('iltf_index'))

    bndry = models.boundary.objects.all()
    documents = models.Document.objects.all()
    upload_files = next(os.walk(os.path.join(os.path.dirname(path), 'media/bmic/uploaded')))[2]
    upload_list = []

    for up_file in upload_files:

        if up_file != ".DS_Store":

            up_file_path = os.path.join(os.path.dirname(path), 'media/bmic/uploaded/', up_file)
            raw_doc_json = open(os.path.join(os.path.dirname(path), 'media/bmic/uploaded/', up_file)).read()
            upload_list.append(raw_doc_json)

    doc_counter = 1

    for document in documents:
        doc_counter += 1

    return render(request, 'bmic/index.html', {
        'title': 'Santa Ana Pueblo of NM',
        'bndry': bndry,
        'documents': documents
    })

def home(request):
    return HttpResponseRedirect(urlresolvers.reverse('admin:app_list', args=("bmic/",)))

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
                                      CROSS JOIN bmic_landfire_evt AS evt
                                      WHERE ST_Intersects(p.geom, evt.rast)),
                        evt_class AS (SELECT classes.label
                                      FROM bmic_landfire_classes AS classes
                                      CROSS JOIN evt_point
                                      WHERE classes.value = evt_point.value),
                        ndvi2005 AS (SELECT ST_Value(ndvi2005.rast, geom) AS value
                                      FROM mypoint AS p
                                      CROSS JOIN bmic_ndvi_2005 AS ndvi2005
                                      WHERE ST_Intersects(p.geom, ndvi2005.rast)),
                        ndvi2010 AS (SELECT ST_Value(ndvi2010.rast, geom) AS value
                                      FROM mypoint AS p
                                      CROSS JOIN bmic_ndvi_2010 AS ndvi2010
                                      WHERE ST_Intersects(p.geom, ndvi2010.rast)),
                        ndvi2015 AS (SELECT ST_Value(ndvi2015.rast, geom) AS value
                                      FROM mypoint AS p
                                      CROSS JOIN bmic_ndvi_2015 AS ndvi2015
                                      WHERE ST_Intersects(p.geom, ndvi2015.rast)),
                        agc AS (SELECT ST_Value(agc.rast, geom) AS value
                                      FROM mypoint AS p
                                      CROSS JOIN bmic_forest_agc AS agc
                                      WHERE ST_Intersects(p.geom, agc.rast)),
                        bgc AS (SELECT ST_Value(bgc.rast, geom) AS value
                                      FROM mypoint AS p
                                      CROSS JOIN bmic_forest_bgc AS bgc
                                      WHERE ST_Intersects(p.geom, bgc.rast)),
                        soc AS (SELECT ST_Value(soc.rast, geom) AS value
                                      FROM mypoint AS p
                                      CROSS JOIN bmic_gssurgo_soc AS soc
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
                           FROM bmic_forest_agc AS agc
                             CROSS JOIN poly
                             WHERE (ST_Intersects(poly.geom, agc.rast))),
                       bgc_clip AS (SELECT ST_Union(ST_Clip(bgc.rast, poly.geom)) AS raster
                           FROM bmic_forest_bgc AS bgc
                             CROSS JOIN poly
                             WHERE (ST_Intersects(poly.geom, bgc.rast))),
                       soc_clip AS (SELECT ST_Union(ST_Clip(soc.rast, poly.geom)) AS raster
                           FROM bmic_gssurgo_soc AS soc
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

                download_file = open(os.path.join(os.path.dirname(path), 'media/bmic/uploaded/boundary.geojson'), "rb")
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

                        download_file = open(os.path.join(os.path.dirname(path), "media/bmic/uploaded/", short_name), "rb")
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

                file_path = os.path.join('bmic/uploaded/', this_file.name)

                filename = re.sub('\.geojson$', '', this_file.name)

                newdoc = models.Document(docfile = request.FILES['docfile'], name=filename)
                newdoc.save()

                documents = models.Document.objects.all()

                return HttpResponseRedirect(reverse('bmic_index'))

        return render(request, 'bmic_index')

    else:
        form = DocumentForm()       # Empty

    # Load documents from the list page

    context = {'documents' : documents, 'form' : form}

    return render(request, 'bmic_index', context)

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

        return HttpResponseRedirect(reverse('bmic_index'))


def delete_up_view(request):

    i = 0
    documents = models.Document.objects.all()
    for document in documents:

        i += 1

        os.remove(os.path.join(settings.MEDIA_ROOT, document.docfile.name))
        document.delete()

    return HttpResponseRedirect(reverse('bmic_index'))

# Logout

def signout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('iltf_index'))


def simplify_geom(model):

    query = """SELECT ST_SimplifyVW(geom, 0.0001) FROM %s;""" %(model)

    conn = psycopg2.connect("dbname='iltf' user='postgres' password='sig_pass'")
    cur = conn.cursor()
    cur.execute(query)
    results = cur.fetchall()

    conn.close()

    return(results)




## Layer Views

def lake_sprior_grid_view(request):
    lake_sprior_grid_json = serialize('geojson', models.lake_sprior_grid.objects.all(), geometry_field='geom', fields = ('grid_no', 'lake_trout', 'wfmu', 'geom', 'id'))
    return HttpResponse(lake_sprior_grid_json, content_type='json')

def golf_course_view(request):
    golf_course_json = serialize('geojson', models.golf_course.objects.all(), geometry_field='geom', fields = ('geom', 'id'))
    return HttpResponse(golf_course_json, content_type='json')

def pwr_syst_backup_2014_view(request):
    pwr_syst_backup_2014_json = serialize('geojson', models.pwr_syst_backup_2014.objects.all(), geometry_field='geom', fields = ('objectid', 'lot_id', 'address', 'name', 'tank_size', 'last_pumpe', 'pass_fail', 'inspection', 'notes', 'ft_from_wa', 'rstre', 'drainfield', 'drainfi8el', 'class_type', 'city', 'state', 'powts', 'yr_cnstrtd', 'qstnre_cmp', 'occupnts_c', 'occupnts_a', 'vacant_mon', 'nmbr_bedro', 'water_mete', 'backup', 'system_rep', 'inspcted_o', 'inspcted_w', 'inspcted_f', 'service_co', 'srvc_cntrc', 'tnk_last_p', 'pump_frequ', 'pump_compa', 'size_gal_g', 'pump_gpm_t', 'pretreat_g', 'pump2_gpm_field', 'soil_trt_u', 'graywtr_sy', 'observatio', 'tank_mater', 'inletbaffl', 'warning_la', 'locate_cov', 'cover_secu', 'srfc_wtr_i', 'fail_indic', 'inspect_li', 'effluent_f', 'run_op_tes', 'gall_added', 'pump_out_p', 'backflow_c', 'inspect_pr', 'inspect_ba', 'dosing_pum', 'integrity_field', 'pump_eleva', 'pump_work', 'checkvalve', 'high_water', 'alarm_work', 'electrical', 'clean_pump', 'probe_soil', 'gravity_pr', 'previous_f', 'seepage', 'lush_veget', 'ponding', 'even_distr', 'feet_to_we', 'groundwate', 'depth_to_s', 'pretreatme', 'pretreat_1', 'pretreat_2', 'soil_treat', 'soil_area_field', 'pump_tank', 'pump_tank_field', 'inspector', 'inspecti_1', 'data_entry', 'data_ent_1', 'latitude', 'longitude', 'geom', 'id'))
    return HttpResponse(pwr_syst_backup_2014_json, content_type='json')

def waiska_watershed_view(request):
    waiska_watershed_json = serialize('geojson', models.waiska_watershed.objects.all(), geometry_field='geom', fields = ('oid_field', 'name', 'folderpath', 'symbolid', 'altitudemo', 'clamped', 'extruded', 'snippet', 'popupinfo', 'shape_leng', 'shape_area', 'geom', 'id'))
    return HttpResponse(waiska_watershed_json, content_type='json')

def aoc_mi_stmarys_view(request):
    aoc_mi_stmarys_json = serialize('geojson', models.aoc_mi_stmarys.objects.all(), geometry_field='geom', fields = ('aoc', 'state', 'geom', 'id'))
    return HttpResponse(aoc_mi_stmarys_json, content_type='json')

def chippewa_cnty_view(request):
    chippewa_cnty_json = serialize('geojson', models.chippewa_cnty.objects.all(), geometry_field='geom', fields = ('statefp', 'countyfp', 'countyns', 'affgeoid', 'geoid', 'name', 'lsad', 'aland', 'awater', 'geom', 'id'))
    return HttpResponse(chippewa_cnty_json, content_type='json')

def snowmobile_trails_view(request):
    snowmobile_trails_json = serialize('geojson', models.snowmobile_trails.objects.all(), geometry_field='geom', fields = ('date', 'time', 'gps_date', 'gps_length', 'geom', 'id'))
    return HttpResponse(snowmobile_trails_json, content_type='json')

def mi_lakes_view(request):
    mi_lakes_json = serialize('geojson', models.mi_lakes.objects.all(), geometry_field='geom', fields = ('county', 'cfcc', 'landname', 'landpoly', 'inland', 'geom', 'id'))
    return HttpResponse(mi_lakes_json, content_type='json')

def critical_dunes_view(request):
    critical_dunes_json = serialize('geojson', models.critical_dunes.objects.all(), geometry_field='geom', fields = ('objectid', 'acres', 'dune_type', 'code', 'ruleid', 'shapestare', 'shapestlen', 'geom', 'id'))
    return HttpResponse(critical_dunes_json, content_type='json')

def whitefish_bay_reserve_view(request):
    whitefish_bay_reserve_json = serialize('geojson', models.whitefish_bay_reserve.objects.all(), geometry_field='geom', fields = ('acreage', 'new_area', 'geom', 'id'))
    return HttpResponse(whitefish_bay_reserve_json, content_type='json')

def great_lakes_view(request):
    great_lakes_json = serialize('geojson', models.great_lakes.objects.all(), geometry_field='geom', fields = ('name', 'geom', 'id'))
    return HttpResponse(great_lakes_json, content_type='json')

def chippewa_waterwells_view(request):
    chippewa_waterwells_json = serialize('geojson', models.chippewa_waterwells.objects.all(), geometry_field='geom', fields = ('wellid', 'county', 'permit_num', 'township', 'town', 'range', 'section', 'owner_name', 'well_addr', 'well_city', 'well_zip', 'well_depth', 'well_type', 'type_other', 'wel_status', 'status_oth', 'wssn', 'well_num', 'driller_id', 'drill_meth', 'meth_other', 'const_date', 'case_type', 'case_other', 'case_dia', 'case_depth', 'screen_frm', 'screen_to', 'swl', 'flowing', 'aq_type', 'test_depth', 'test_hours', 'test_rate', 'test_methd', 'test_other', 'grout', 'pmp_cpcity', 'latitude', 'longitude', 'methd_coll', 'elevation', 'elev_methd', 'geom', 'id'))
    return HttpResponse(chippewa_waterwells_json, content_type='json')

def boundary_view(request):
    boundary_json = serialize('geojson', models.boundary.objects.all(), geometry_field='geom', fields = ('oid_field', 'name', 'folderpath', 'symbolid', 'altitudemo', 'clamped', 'extruded', 'snippet', 'popupinfo', 'shape_leng', 'shape_area', 'geom', 'id'))
    return HttpResponse(boundary_json, content_type='json')

def subwatersheds_view(request):
    subwatersheds_json = serialize('geojson', models.subwatersheds.objects.all(), geometry_field='geom', fields = ('oid_field', 'name', 'folderpath', 'symbolid', 'altitudemo', 'clamped', 'extruded', 'snippet', 'popupinfo', 'shape_leng', 'shape_area', 'geom', 'id'))
    return HttpResponse(subwatersheds_json, content_type='json')

def coastal_wetlands_view(request):
    coastal_wetlands_json = serialize('geojson', models.coastal_wetlands.objects.all(), geometry_field='geom', fields = ('objectid', 'type', 'area', 'perimeter', 'acres', 'shape_leng', 'shape_area', 'geom', 'id'))
    return HttpResponse(coastal_wetlands_json, content_type='json')

def chippewa_streams_view(request):
    chippewa_streams_json = serialize('geojson', models.chippewa_streams.objects.all(), geometry_field='geom', fields = ('oid_field', 'name', 'folderpath', 'symbolid', 'altitudemo', 'clamped', 'extruded', 'snippet', 'popupinfo', 'shape_leng', 'geom', 'id'))
    return HttpResponse(chippewa_streams_json, content_type='json')

def waishkey_river_view(request):
    waishkey_river_json = serialize('geojson', models.waishkey_river.objects.all(), geometry_field='geom', fields = ('oid_field', 'name', 'folderpath', 'symbolid', 'altitudemo', 'clamped', 'extruded', 'snippet', 'popupinfo', 'shape_leng', 'geom', 'id'))
    return HttpResponse(waishkey_river_json, content_type='json')

def chippewa_roads_view(request):
    chippewa_roads_json = serialize('geojson', models.chippewa_roads.objects.all(), geometry_field='geom', fields = ('fcc', 'rdname', 'fraddl', 'toaddl', 'fraddr', 'toaddr', 'zipl', 'zipr', 'fmcdl', 'fmcdr', 'fedirp', 'name', 'fetype', 'fedirs', 'fedirp2', 'name2', 'fetype2', 'fedirs2', 'fedirp3', 'name3', 'fetype3', 'fedirs3', 'nfc', 'ru_l', 'ru_r', 'legalsyst', 'pr', 'bmp', 'emp', 'bpt', 'ept', 'lrs_link', 'length', 'oid_1', 'ver', 'mgf_hist', 'geom', 'id'))
    return HttpResponse(chippewa_roads_json, content_type='json')

def eup_state_parks_view(request):
    eup_state_parks_json = serialize('geojson', models.eup_state_parks.objects.all(), geometry_field='geom', fields = ('objectid', 'acres', 'district', 'facility', 'geom', 'id'))
    return HttpResponse(eup_state_parks_json, content_type='json')

def mi_cntys_view(request):
    mi_cntys_json = serialize('geojson', models.mi_cntys.objects.all(), geometry_field='geom', fields = ('area', 'perimeter', 'cnty_fips', 'st_fips', 'fipsstco', 'name', 'name2', 'totpop', 'total_ai', 'geom', 'id'))
    return HttpResponse(mi_cntys_json, content_type='json')

def ceded_territory_view(request):
    ceded_territory_json = serialize('geojson', models.ceded_territory.objects.all(), geometry_field='geom', fields = ('area', 'perimeter', 'ceaded2_field', 'ceaded2_id', 'geom', 'id'))
    return HttpResponse(ceded_territory_json, content_type='json')

def railroad_view(request):
    railroad_json = serialize('geojson', models.railroad.objects.all(), geometry_field='geom', fields = ('fcc', 'name', 'name2', 'name3', 'length', 'oid', 'mgf_hist', 'geom', 'id'))
    return HttpResponse(railroad_json, content_type='json')

def waishkey_add_streams_view(request):
    waishkey_add_streams_json = serialize('geojson', models.waishkey_add_streams.objects.all(), geometry_field='geom', fields = ('fcc', 'name', 'name2', 'name3', 'length', 'oid_1', 'ver', 'mgf_hist', 'geom', 'id'))
    return HttpResponse(waishkey_add_streams_json, content_type='json')

def wastewater_lines_view(request):
    wastewater_lines_json = serialize('geojson', models.wastewater_lines.objects.all(), geometry_field='geom', fields = ('objectid', 'type', 'size', 'constructi', 'repair_dat', 'contractor', 'original_c', 'replacemen', 'flow_vol', 'shape_leng', 'geom', 'id'))
    return HttpResponse(wastewater_lines_json, content_type='json')

def watermains_view(request):
    watermains_json = serialize('geojson', models.watermains.objects.all(), geometry_field='geom', fields = ('id', 'rdname', 'cnt_rdname', 'irr', 'route_95', 'class_95', 'constru_95', 'surface_95', 'owner_95', 'sect_95', 'sec_nam_95', 'z5_length', 'z3_surface', 'z3_conditi', 'z3_constru', 'z3_owner', 'z3_other', 'on_reserva', 'length', 'length_mil', 'need_01', 'wtrmn_clss', 'pro_surfac', 'pro_should', 'pro_width', 'cost', 'length2010'))
    return HttpResponse(watermains_json, content_type='json')

def waishkey_ptnl_wtlnd_rstrn_view(request):
    waishkey_ptnl_wtlnd_rstrn_json = serialize('geojson', models.waishkey_ptnl_wtlnd_rstrn.objects.all(), geometry_field='geom', fields = ('objectid_1', 'objectid', 'res_rank', 'acres', 'area_field', 'shape_star', 'shape_stle', 'shapestare', 'shapestlen', 'geom', 'id'))
    return HttpResponse(waishkey_ptnl_wtlnd_rstrn_json, content_type='json')

def e_hiawathanf_view(request):
    e_hiawathanf_json = serialize('geojson', models.e_hiawathanf.objects.all(), geometry_field='geom', fields = ('objectid', 'gisacres', 'rev_date', 'shape_area', 'shape_len', 'type_class', 'geom', 'id'))
    return HttpResponse(e_hiawathanf_json, content_type='json')

def comm_forst_ceded_view(request):
    comm_forst_ceded_json = serialize('geojson', models.comm_forst_ceded.objects.all(), geometry_field='geom', fields = ('landowner', 'legal_acre', 'input_id', 'grouped', 'county', 'geom', 'id'))
    return HttpResponse(comm_forst_ceded_json, content_type='json')

def rivers_view(request):
    #with open('/home/jbukoski/consulting/sig/geodjango/iltf/data/bmic/rivers.geojson') as f:
    #    data = json.load(f)
    #print(data)
    rivers_json = serialize('geojson', models.rivers.objects.all(), geometry_field='geom', fields = ('fid', 'name', 'oid_1', 'ver', 'mgf_hist', 'length', 'fcc', 'name2', 'name3', 'fid2', 'geom', 'id'))
    return HttpResponse(data, content_type='json')

def wellhead_protection_view(request):
    wellhead_protection_json = serialize('geojson', models.wellhead_protection.objects.all(), geometry_field='geom', fields = ('objectid', 'michiganwe', 'wssn', 'system', 'type', 'approval_d', 'shapestare', 'shapestlen', 'geom', 'id'))
    return HttpResponse(wellhead_protection_json, content_type='json')

def mi_state_parks_view(request):
    mi_state_parks_json = serialize('geojson', models.mi_state_parks.objects.all(), geometry_field='geom', fields = ('objectid', 'acres', 'district', 'facility', 'geom', 'id'))
    return HttpResponse(mi_state_parks_json, content_type='json')

def buffered_bndry_view(request):
    buffered_bndry_json = serialize('geojson', models.buffered_bndry.objects.all(), geometry_field='geom', fields = ('geom', 'id'))
    return HttpResponse(buffered_bndry_json, content_type='json')

def ir_roads_view(request):
    ir_roads_json = serialize('geojson', models.ir_roads.objects.all(), geometry_field='geom', fields = ('rdname', 'cnt_rdname', 'irr', 'route_95', 'class_95', 'constru_95', 'surface_95', 'owner_95', 'sect_95', 'sec_nam_95', 'z5_length', 'z3_surface', 'z3_conditi', 'z3_constru', 'z3_owner', 'z3_other', 'on_reserva', 'length', 'length_mil', 'need_01', 'type_class', 'pro_surfac', 'pro_should', 'pro_width', 'cost', 'length2010', 'geom', 'id'))
    return HttpResponse(ir_roads_json, content_type='json')

def parcels_view(request):
    parcels_json = serialize('geojson', models.parcels.objects.all(), geometry_field='geom', fields = ('area', 'perimeter', 'lots3_field', 'address', 'acres', 'street', 'street_typ', 'street_2', 'c_address', 'label', 'svc_ln_upd', 'flow_dir', 'geom', 'id'))
    return HttpResponse(parcels_json, content_type='json')

def wetland_preserve_view(request):
    wetland_preserve_json = serialize('geojson', models.wetland_preserve.objects.all(), geometry_field='geom', fields = ('area', 'perimeter', 'chippewa_field', 'chippewa_i', 'county', 'range', 'town', 'section', 'qtr_qtr', 'qtr', 'twnrng', 'twnrngsec', 'geo_id', 'cnty2', 'forty', 'gov_lot', 'claim', 'x_coord', 'y_coord', 'other', 'acreage', 'new_area', 'geom', 'id'))
    return HttpResponse(wetland_preserve_json, content_type='json')

## Layer Download Views

## Raster Download Views

def bmic_forest_agc_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'bmic_forest_agc.tif'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="bmic_forest_agc.zip"'

    return response

def bmic_forest_bgc_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'bmic_forest_bgc.tif'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="bmic_forest_bgc.zip"'

    return response

def bmic_gssurgo_soc_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'bmic_soc.tif'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="bmic_gssurgo_soc.zip"'

    return response

def bmic_landfire_evt_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'bmic_evt.tif'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="bmic_landfire_evt.zip"'

    return response

def bmic_ndvi_2005_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'bmic_ndvi_2005.tif'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="bmic_ndvi_2005.zip"'

    return response

def bmic_ndvi_2010_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'bmic_ndvi_2010.tif'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="bmic_ndvi_2010.zip"'

    return response

def bmic_ndvi_2015_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'bmic_ndvi_2015.tif'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="bmic_ndvi_2015.zip"'

    return response


## Vector Download Views

def lake_sprior_grid_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'lake_sprior_grid.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="lake_sprior_grid.zip"'

    return response
  
def golf_course_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'golf_course.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="golf_course.zip"'

    return response
  
def pwr_syst_backup_2014_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'pwr_syst_backup_2014.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="pwr_syst_backup_2014.zip"'

    return response
  
def waiska_watershed_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'waiska_watershed.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="waiska_watershed.zip"'

    return response
  
def aoc_mi_stmarys_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'aoc_mi_stmarys.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="aoc_mi_stmarys.zip"'

    return response
  
def chippewa_cnty_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'chippewa_cnty.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="chippewa_cnty.zip"'

    return response
  
def snowmobile_trails_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'snowmobile_trails.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="snowmobile_trails.zip"'

    return response
  
def mi_lakes_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'mi_lakes.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="mi_lakes.zip"'

    return response
  
def critical_dunes_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'critical_dunes.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="critical_dunes.zip"'

    return response
  
def whitefish_bay_reserve_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'whitefish_bay_reserve.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="whitefish_bay_reserve.zip"'

    return response
  
def great_lakes_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'great_lakes.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="great_lakes.zip"'

    return response
  
def chippewa_waterwells_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'chippewa_waterwells.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="chippewa_waterwells.zip"'

    return response
  
def boundary_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'boundary.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="boundary.zip"'

    return response
  
def subwatersheds_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'subwatersheds.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="subwatersheds.zip"'

    return response
  
def coastal_wetlands_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'coastal_wetlands.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="coastal_wetlands.zip"'

    return response
  
def chippewa_streams_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'chippewa_streams.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="chippewa_streams.zip"'

    return response
  
def waishkey_river_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'waishkey_river.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="waishkey_river.zip"'

    return response
  
def chippewa_roads_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'chippewa_roads.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="chippewa_roads.zip"'

    return response
  
def eup_state_parks_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'eup_state_parks.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="eup_state_parks.zip"'

    return response
  
def mi_cntys_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'mi_cntys.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="mi_cntys.zip"'

    return response
  
def ceded_territory_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'ceded_territory.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="ceded_territory.zip"'

    return response
  
def railroad_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'railroad.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="railroad.zip"'

    return response
  
def document_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'document.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="document.zip"'

    return response
  
def waishkey_add_streams_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'waishkey_add_streams.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="waishkey_add_streams.zip"'

    return response
  
def wastewater_lines_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'wastewater_lines.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="wastewater_lines.zip"'

    return response
  
def waishkey_ptnl_wtlnd_rstrn_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'waishkey_ptnl_wtlnd_rstrn.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="waishkey_ptnl_wtlnd_rstrn.zip"'

    return response

def watermains_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'watermains.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="watermains.zip"'

    return response
  
def e_hiawathanf_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'e_hiawathanf.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="e_hiawathanf.zip"'

    return response
  
def comm_forst_ceded_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'comm_forst_ceded.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="comm_forst_ceded.zip"'

    return response
  
def rivers_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'rivers.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="rivers.zip"'

    return response
  
def wellhead_protection_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'wellhead_protection.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="wellhead_protection.zip"'

    return response
  
def mi_state_parks_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'mi_state_parks.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="mi_state_parks.zip"'

    return response
  
def buffered_bndry_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'buffered_bndry.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="buffered_bndry.zip"'

    return response
  
def ir_roads_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'ir_roads.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="ir_roads.zip"'

    return response
  
def parcels_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'parcels.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="parcels.zip"'

    return response
  
def wetland_preserve_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'wetland_preserve.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="wetland_preserve.zip"'

    return response

def trails_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'trails.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="trails.zip"'

    return response

def drainfields_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'drainfields.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="drainfields.zip"'

    return response

def onsitewaste_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'onsitewaste.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="onsitewaste.zip"'

    return response

def onsitewastewater_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'onsitewastewater.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="onsitewastewater.zip"'

    return response

def septic_tanks_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'bmic', 'septic_tanks.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="septic_tanks.zip"'

    return response

