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

from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_protect

# Raster interaction views:


@csrf_protect
def legend_view(request):

    if request.method == 'POST':
        lat = request.POST['lat']
        lon = request.POST['lng']

        query = """WITH mypoint AS (SELECT ST_SetSRID(ST_MakePoint(%s, %s), 4326) geom),
                        evt_point AS (SELECT ST_Value(evt.rast, geom) AS value
                                      FROM mypoint AS p 
                                      CROSS JOIN calc_landfire_evt AS evt
                                      WHERE ST_Intersects(p.geom, evt.rast)),
                        evt_class AS (SELECT classes.label
                                      FROM calc_landfire_classes AS classes
                                      CROSS JOIN evt_point
                                      WHERE classes.value = evt_point.value),
                        ndvi2005 AS (SELECT ST_Value(ndvi2005.rast, geom) AS value
                                      FROM mypoint AS p
                                      CROSS JOIN calc_ndvi_2005 AS ndvi2005
                                      WHERE ST_Intersects(p.geom, ndvi2005.rast)),
                        ndvi2010 AS (SELECT ST_Value(ndvi2010.rast, geom) AS value
                                      FROM mypoint AS p
                                      CROSS JOIN calc_ndvi_2010 AS ndvi2010
                                      WHERE ST_Intersects(p.geom, ndvi2010.rast)),
                        ndvi2015 AS (SELECT ST_Value(ndvi2015.rast, geom) AS value
                                      FROM mypoint AS p
                                      CROSS JOIN calc_ndvi_2015 AS ndvi2015
                                      WHERE ST_Intersects(p.geom, ndvi2015.rast)),
                        agc AS (SELECT ST_Value(agc.rast, geom) AS value
                                      FROM mypoint AS p
                                      CROSS JOIN calc_forest_agc AS agc
                                      WHERE ST_Intersects(p.geom, agc.rast)),
                        bgc AS (SELECT ST_Value(bgc.rast, geom) AS value
                                      FROM mypoint AS p
                                      CROSS JOIN calc_forest_bgc AS bgc
                                      WHERE ST_Intersects(p.geom, bgc.rast)),
                        soc AS (SELECT ST_Value(soc.rast, geom) AS value
                                      FROM mypoint AS p
                                      CROSS JOIN calc_gssurgo_soc AS soc
                                      WHERE ST_Intersects(p.geom, soc.rast))
                        SELECT *
                        FROM evt_point, evt_class, ndvi2005, ndvi2010, ndvi2015, agc, bgc, soc; """ % (lon, lat)

        conn = psycopg2.connect("dbname='iltf' user='postgres' password='sig_pass'")
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()

        print("\n\n", results, "\n\n")

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

        print("\n\n", legText, "\n\n")

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
                           FROM calc_forest_agc AS agc
                             CROSS JOIN poly
                             WHERE (ST_Intersects(poly.geom, agc.rast))),
                       bgc_clip AS (SELECT ST_Union(ST_Clip(bgc.rast, poly.geom)) AS raster
                           FROM calc_forest_bgc AS bgc
                             CROSS JOIN poly
                             WHERE (ST_Intersects(poly.geom, bgc.rast))),
                       soc_clip AS (SELECT ST_Union(ST_Clip(soc.rast, poly.geom)) AS raster
                           FROM calc_gssurgo_soc AS soc
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

        conn = psycopg2.connect("dbname='iltf' user='postgres' password='sig_pass'")
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
            
        print("\n\n=======In Calc Sumstats View=======")
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

