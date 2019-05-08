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
     
    if not request.user.username == 'jskt_user':
        return HttpResponseRedirect(reverse('iltf_index'))

    bndry = models.boundary.objects.all()
    documents = models.Document.objects.all()
    upload_files = next(os.walk(os.path.join(os.path.dirname(path), 'media/jskt/uploaded')))[2]
    upload_list = []

    for up_file in upload_files:

        if up_file != ".DS_Store":

            up_file_path = os.path.join(os.path.dirname(path), 'media/jskt/uploaded/', up_file)
            raw_doc_json = open(os.path.join(os.path.dirname(path), 'media/jskt/uploaded/', up_file)).read()
            upload_list.append(raw_doc_json)

    doc_counter = 1

    for document in documents:
        doc_counter += 1

    return render(request, 'jskt/index.html', {
        'title': "Jamestown S'Klallam Tribe",
        'bndry': bndry,
        'documents': documents
    })

def home(request):
    return HttpResponseRedirect(urlresolvers.reverse('admin:app_list', args=("jskt/",)))

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
                                      CROSS JOIN jskt_landfire_evt AS evt
                                      WHERE ST_Intersects(p.geom, evt.rast)),
                        evt_class AS (SELECT classes.label
                                      FROM jskt_landfire_classes AS classes
                                      CROSS JOIN evt_point
                                      WHERE classes.value = evt_point.value),
                        ndvi2005 AS (SELECT ST_Value(ndvi2005.rast, geom) AS value
                                      FROM mypoint AS p
                                      CROSS JOIN jskt_ndvi_2005 AS ndvi2005
                                      WHERE ST_Intersects(p.geom, ndvi2005.rast)),
                        ndvi2010 AS (SELECT ST_Value(ndvi2010.rast, geom) AS value
                                      FROM mypoint AS p
                                      CROSS JOIN jskt_ndvi_2010 AS ndvi2010
                                      WHERE ST_Intersects(p.geom, ndvi2010.rast)),
                        ndvi2015 AS (SELECT ST_Value(ndvi2015.rast, geom) AS value
                                      FROM mypoint AS p
                                      CROSS JOIN jskt_ndvi_2015 AS ndvi2015
                                      WHERE ST_Intersects(p.geom, ndvi2015.rast)),
                        agc AS (SELECT ST_Value(agc.rast, geom) AS value
                                      FROM mypoint AS p
                                      CROSS JOIN jskt_forest_agc AS agc
                                      WHERE ST_Intersects(p.geom, agc.rast)),
                        bgc AS (SELECT ST_Value(bgc.rast, geom) AS value
                                      FROM mypoint AS p
                                      CROSS JOIN jskt_forest_bgc AS bgc
                                      WHERE ST_Intersects(p.geom, bgc.rast)),
                        soc AS (SELECT ST_Value(soc.rast, geom) AS value
                                      FROM mypoint AS p
                                      CROSS JOIN jskt_gssurgo_soc AS soc
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
                           FROM jskt_forest_agc AS agc
                             CROSS JOIN poly
                             WHERE (ST_Intersects(poly.geom, agc.rast))),
                       bgc_clip AS (SELECT ST_Union(ST_Clip(bgc.rast, poly.geom)) AS raster
                           FROM jskt_forest_bgc AS bgc
                             CROSS JOIN poly
                             WHERE (ST_Intersects(poly.geom, bgc.rast))),
                       soc_clip AS (SELECT ST_Union(ST_Clip(soc.rast, poly.geom)) AS raster
                           FROM jskt_gssurgo_soc AS soc
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

                download_file = open(os.path.join(os.path.dirname(path), 'media/jskt/uploaded/boundary.geojson'), "rb")
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

                        download_file = open(os.path.join(os.path.dirname(path), "media/jskt/uploaded/", short_name), "rb")
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

                file_path = os.path.join('jskt/uploaded/', this_file.name)

                filename = re.sub('\.geojson$', '', this_file.name)

                newdoc = models.Document(docfile = request.FILES['docfile'], name=filename)
                newdoc.save()

                documents = models.Document.objects.all()

                return HttpResponseRedirect(reverse('jskt_index'))

        return render(request, 'jskt_index')

    else:
        form = DocumentForm()       # Empty

    # Load documents from the list page

    context = {'documents' : documents, 'form' : form}

    return render(request, 'jskt_index', context)

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

        return HttpResponseRedirect(reverse('jskt_index'))


def delete_up_view(request):

    i = 0
    documents = models.Document.objects.all()
    for document in documents:

        i += 1

        os.remove(os.path.join(settings.MEDIA_ROOT, document.docfile.name))
        document.delete()

    return HttpResponseRedirect(reverse('jskt_index'))

# Logout

def signout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('iltf_index'))

## Layer Views

def cl_co_prop_db_view(request):
    cl_co_prop_db_json = serialize('geojson', models.cl_co_prop_db.objects.all(), geometry_field='geom', fields = ('pnum', 'version', 'prop_id', 'pacs_info', 'acres_gis', 'acres_surv', 'area_sf', 'status', 'prc_status', 'owners', 'situs_addr', 'situs_dir', 'situs_rd', 'situs_ext', 'situs_city', 'cdate', 'edit_date', 'mdoc_date', 'mdoc_afn', 'mdoc_typcd', 'mdoc_type', 'vol', 'page', 'lot', 'block', 'tideland', 'tide_statu', 'value_land', 'value_impr', 'mkt_value', 'luse_res', 'ludesc_res', 'acres_res', 'luse_os', 'ludesc_os', 'acres_os', 'luse_oth', 'ludesc_oth', 'acres_oth', 'value_res', 'value_os', 'value_oth', 'prc_class', 'rgn', 'region', 'sub_region', 'zoning', 'zon_pct', 'zon_rmd', 'city', 'zip_code', 'uga', 'lamird', 'tax_area', 'levy', 'fire_dist', 'school', 'mra', 'wr_code', 'pwsid', 'pws_group', 'irrig', 'rts', 'qp', 'label', 'geo_12', 'pn12', 'rdate', 'rdoc_afn', 'pacs_link', 'pmt_link', 'tribal', 'sort_by', 'ownership', 'owner_nm', 'owner_addr', 'owner_city', 'owner_st', 'owner_zip', 'jskt_statu', 'prev_owner', 'trust_num', 'survey', 'comments', 'year_purch', 'site_work', 'inventory', 'explana_field', 'trust_da', 'perimeter', 'area', 'acres', 'reser_num', 'rentaltype', 'shape_leng', 'shape_area', 'geom', 'id'))
    return HttpResponse(cl_co_prop_db_json, content_type='json')

def fee_trust_view(request):
    fee_trust_json = serialize('geojson', models.fee_trust.objects.all(), geometry_field='geom', fields = ('pnum', 'version', 'prop_id', 'pacs_info', 'acres_gis', 'acres_surv', 'area_sf', 'status', 'prc_status', 'owners', 'situs_addr', 'situs_dir', 'situs_rd', 'situs_ext', 'situs_city', 'cdate', 'edit_date', 'mdoc_date', 'mdoc_afn', 'mdoc_typcd', 'mdoc_type', 'vol', 'page', 'lot', 'block', 'tideland', 'tide_statu', 'value_land', 'value_impr', 'mkt_value', 'luse_res', 'ludesc_res', 'acres_res', 'luse_os', 'ludesc_os', 'acres_os', 'luse_oth', 'ludesc_oth', 'acres_oth', 'value_res', 'value_os', 'value_oth', 'prc_class', 'rgn', 'region', 'sub_region', 'zoning', 'zon_pct', 'zon_rmd', 'city', 'zip_code', 'uga', 'lamird', 'tax_area', 'levy', 'fire_dist', 'school', 'mra', 'wr_code', 'pwsid', 'pws_group', 'irrig', 'rts', 'qp', 'label', 'geo_12', 'pn12', 'rdate', 'rdoc_afn', 'pacs_link', 'pmt_link', 'tribal', 'sort_by', 'ownership', 'owner_nm', 'owner_addr', 'owner_city', 'owner_st', 'owner_zip', 'jskt_statu', 'prev_owner', 'trust_num', 'survey', 'comments', 'year_purch', 'site_work', 'inventory', 'explana_field', 'trust_da', 'perimeter', 'area', 'acres', 'reser_num', 'rentaltype', 'shape_leng', 'shape_area', 'geom', 'id'))
    return HttpResponse(fee_trust_json, content_type='json')

def service_area_view(request):
    service_area_json = serialize('geojson', models.service_area.objects.all(), geometry_field='geom', fields = ('fid_pttown', 'data', 'fid_servic', 'area', 'shape_leng', 'shape_area', 'geom', 'id'))
    return HttpResponse(service_area_json, content_type='json')

def jef_co_prop_db_view(request):
    jef_co_prop_db_json = serialize('geojson', models.jef_co_prop_db.objects.all(), geometry_field='geom', fields = ('objectid', 'pin', 'pin_string', 'land_use', 'lu_desc', 'prop_id', 'av_year', 'owner_id', 'owner_name', 'state_code', 'tax_code', 'school_dis', 'fire_dist', 'planning_a', 'ttl_acres', 'legal_desc', 'cycle', 'hood_code', 'hood_desc', 'subdv_code', 'subdv_desc', 'township', 'range', 'section_field', 'qtr_sectio', 'situs_addr', 'situs_city', 'situs_zip', 'certifiedf', 'cfmv_imps', 'cfmv_land', 'cfmv_total', 'notes', 'sale_reet', 'sale_deed', 'sale_price', 'sale_date', 'sale_multi', 'sale_rcode', 'sale_rdesc', 'down_date', 'buildingph', 'globalid', 'pacsweb_ye', 'shapearea', 'shapelen', 'owner', 'status', 'prev_own', 'sort_by', 'perimeter', 'area', 'acres', 'shape_leng', 'shape_area', 'geom', 'id'))
    return HttpResponse(jef_co_prop_db_json, content_type='json')

def boundary_view(request):
    boundary_json = serialize('geojson', models.boundary.objects.all(), geometry_field='geom', fields = ('aiannhce', 'aiannhns', 'affgeoid', 'geoid', 'name', 'lsad', 'aland', 'awater', 'geom', 'id'))
    return HttpResponse(boundary_json, content_type='json')

def counties_view(request):
    counties_json = serialize('geojson', models.counties.objects.all(), geometry_field='geom', fields = ('objectid', 'name', 'state_name', 'state_fips', 'cnty_fips', 'fips', 'population', 'pop_sqmi', 'pop2010', 'pop10_sqmi', 'white', 'black', 'ameri_es', 'asian', 'hawn_pi', 'hispanic', 'other', 'mult_race', 'males', 'females', 'age_under5', 'age_5_9', 'age_10_14', 'age_15_19', 'age_20_24', 'age_25_34', 'age_35_44', 'age_45_54', 'age_55_64', 'age_65_74', 'age_75_84', 'age_85_up', 'med_age', 'med_age_m', 'med_age_f', 'households', 'ave_hh_sz', 'hsehld_1_m', 'hsehld_1_f', 'marhh_chd', 'marhh_no_c', 'mhh_child', 'fhh_child', 'families', 'ave_fam_sz', 'hse_units', 'vacant', 'owner_occ', 'renter_occ', 'no_farms12', 'ave_size12', 'crop_acr12', 'ave_sale12', 'sqmi', 'shape_leng', 'shape_area', 'geom', 'id'))
    return HttpResponse(counties_json, content_type='json')

def buff_bndry_view(request):
    buff_bndry_json = serialize('geojson', models.buff_bndry.objects.all(), geometry_field='geom', fields = ('objectid', 'geom', 'id'))
    return HttpResponse(buff_bndry_json, content_type='json')

def land_consolidation_view(request):
    land_consolidation_json = serialize('geojson', models.land_consolidation.objects.all(), geometry_field='geom', fields = ('fid_pttown', 'data', 'fid_servic', 'area', 'shape_leng', 'shape_area', 'geom', 'id'))
    return HttpResponse(land_consolidation_json, content_type='json')

def document_view(request):
    document_json = serialize('geojson', models.document.objects.all(), geometry_field='geom', fields = ('id', 'name', 'docfile'))
    return HttpResponse(document_json, content_type='json')

def prop_only_view(request):
    prop_only_json = serialize('geojson', models.prop_only.objects.all(), geometry_field='geom', fields = ('objectid', 'pin', 'pin_string', 'land_use', 'lu_desc', 'prop_id', 'av_year', 'owner_id', 'owner_name', 'state_code', 'tax_code', 'school_dis', 'fire_dist', 'planning_a', 'ttl_acres', 'legal_desc', 'cycle', 'hood_code', 'hood_desc', 'subdv_code', 'subdv_desc', 'township', 'range', 'section_field', 'qtr_sectio', 'situs_addr', 'situs_city', 'situs_zip', 'certifiedf', 'cfmv_imps', 'cfmv_land', 'cfmv_total', 'notes', 'sale_reet', 'sale_deed', 'sale_price', 'sale_date', 'sale_multi', 'sale_rcode', 'sale_rdesc', 'down_date', 'buildingph', 'globalid', 'pacsweb_ye', 'shapearea', 'shapelen', 'owner', 'status', 'prev_own', 'sort_by', 'perimeter', 'area', 'acres', 'shape_leng', 'shape_area', 'geom', 'id'))
    return HttpResponse(prop_only_json, content_type='json')

def res_trust_view(request):
    res_trust_json = serialize('geojson', models.res_trust.objects.all(), geometry_field='geom', fields = ('pnum', 'version', 'prop_id', 'pacs_info', 'acres_gis', 'acres_surv', 'area_sf', 'status', 'prc_status', 'owners', 'situs_addr', 'situs_dir', 'situs_rd', 'situs_ext', 'situs_city', 'cdate', 'edit_date', 'mdoc_date', 'mdoc_afn', 'mdoc_typcd', 'mdoc_type', 'vol', 'page', 'lot', 'block', 'tideland', 'tide_statu', 'value_land', 'value_impr', 'mkt_value', 'luse_res', 'ludesc_res', 'acres_res', 'luse_os', 'ludesc_os', 'acres_os', 'luse_oth', 'ludesc_oth', 'acres_oth', 'value_res', 'value_os', 'value_oth', 'prc_class', 'rgn', 'region', 'sub_region', 'zoning', 'zon_pct', 'zon_rmd', 'city', 'zip_code', 'uga', 'lamird', 'tax_area', 'levy', 'fire_dist', 'school', 'mra', 'wr_code', 'pwsid', 'pws_group', 'irrig', 'rts', 'qp', 'label', 'geo_12', 'pn12', 'rdate', 'rdoc_afn', 'pacs_link', 'pmt_link', 'tribal', 'sort_by', 'ownership', 'owner_nm', 'owner_addr', 'owner_city', 'owner_st', 'owner_zip', 'jskt_statu', 'prev_owner', 'trust_num', 'survey', 'comments', 'year_purch', 'site_work', 'inventory', 'explana_field', 'trust_da', 'perimeter', 'area', 'acres', 'reser_num', 'rentaltype', 'shape_leng', 'shape_area', 'geom', 'id'))
    return HttpResponse(res_trust_json, content_type='json')

def all_prop_view(request):
    all_prop_json = serialize('geojson', models.all_prop.objects.all(), geometry_field='geom', fields = ('pnum', 'version', 'prop_id', 'pacs_info', 'acres_gis', 'acres_surv', 'area_sf', 'status', 'prc_status', 'owners', 'situs_addr', 'situs_dir', 'situs_rd', 'situs_ext', 'situs_city', 'cdate', 'edit_date', 'mdoc_date', 'mdoc_afn', 'mdoc_typcd', 'mdoc_type', 'vol', 'page', 'lot', 'block', 'tideland', 'tide_statu', 'value_land', 'value_impr', 'mkt_value', 'luse_res', 'ludesc_res', 'acres_res', 'luse_os', 'ludesc_os', 'acres_os', 'luse_oth', 'ludesc_oth', 'acres_oth', 'value_res', 'value_os', 'value_oth', 'prc_class', 'rgn', 'region', 'sub_region', 'zoning', 'zon_pct', 'zon_rmd', 'city', 'zip_code', 'uga', 'lamird', 'tax_area', 'levy', 'fire_dist', 'school', 'mra', 'wr_code', 'pwsid', 'pws_group', 'irrig', 'rts', 'qp', 'label', 'geo_12', 'pn12', 'rdate', 'rdoc_afn', 'pacs_link', 'pmt_link', 'tribal', 'sort_by', 'ownership', 'owner_nm', 'owner_addr', 'owner_city', 'owner_st', 'owner_zip', 'jskt_statu', 'prev_owner', 'trust_num', 'survey', 'comments', 'year_purch', 'site_work', 'inventory', 'explana_field', 'trust_da', 'perimeter', 'area', 'acres', 'reser_num', 'rentaltype', 'shape_leng', 'shape_area', 'geom', 'id'))
    return HttpResponse(all_prop_json, content_type='json')

## Layer Download Views

def cl_co_prop_db_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'jskt', 'cl_co_prop_db.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="cl_co_prop_db.zip"'

    return response
  
def fee_trust_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'jskt', 'fee_trust.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="fee_trust.zip"'

    return response
  
def service_area_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'jskt', 'service_area.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="service_area.zip"'

    return response
  
def jef_co_prop_db_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'jskt', 'jef_co_prop_db.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="jef_co_prop_db.zip"'

    return response
  
def boundary_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'jskt', 'boundary.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="boundary.zip"'

    return response
  
def counties_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'jskt', 'counties.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="counties.zip"'

    return response
  
def buff_bndry_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'jskt', 'buff_bndry.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="buff_bndry.zip"'

    return response
  
def land_consolidation_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'jskt', 'land_consolidation.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="land_consolidation.zip"'

    return response
  
def document_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'jskt', 'document.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="document.zip"'

    return response
  
def prop_only_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'jskt', 'prop_only.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="prop_only.zip"'

    return response
  
def res_trust_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'jskt', 'res_trust.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="res_trust.zip"'

    return response
  
def all_prop_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'jskt', 'all_prop.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="all_prop.zip"'

    return response
  
