import os
from django.contrib.gis.utils import LayerMapping
from . import models

boundary_mapping = {
    'sec' : 'Sec',
    't' : 'T',
    'r' : 'R',
    'poly_area' : 'POLY_AREA',
    'area_geo' : 'AREA_GEO',
    'perimeter' : 'PERIMETER',
    'perim_geo' : 'PERIM_GEO',
    'geom' : 'MULTIPOLYGON',
}

boundary_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'shbt', 'boundary.shp'))

districts_mapping = {
    'total_ac' : 'Total_Ac',
    'name' : 'Name',
    'geom' : 'MULTIPOLYGON',
}

districts_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'shbt', 'districts.shp'))

ownership_mapping = {
    'area' : 'AREA',
    'perimeter' : 'PERIMETER',
    'lstmoss_wg' : 'LSTMOSS_WG',
    'lstmoss_1' : 'LSTMOSS_1',
    'lstmoss_at' : 'LSTMOSS_AT',
    'lease_a' : 'LEASE_A',
    'original' : 'ORIGINAL',
    'status' : 'STATUS',
    'lease_b' : 'LEASE_B',
    'lease_c' : 'LEASE_C',
    'key' : 'KEY',
    'recording_field' : 'RECORDING_',
    'key2' : 'KEY2',
    'lease_d' : 'LEASE_D',
    'rpd_num' : 'RPD_NUM',
    'tenant' : 'Tenant',
    'section' : 'Section',
    'township' : 'Township',
    'range' : 'Range',
    'lstatus' : 'LStatus',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'curr_own' : 'CURR_OWN',
    'tribal_int' : 'Tribal_INT',
    'acreage' : 'Acreage',
    'res_code' : 'RES_CODE',
    'trib_own_m' : 'TRIB_OWN_M',
    'trib_own_s' : 'TRIB_OWN_S',
    'poly_area' : 'POLY_AREA',
    'geom' : 'MULTIPOLYGON',
}

ownership_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'shbt', 'ownership.shp'))

range_units_mapping = {
    'area' : 'AREA',
    'perimeter' : 'PERIMETER',
    'rnge_field' : 'RNGE_',
    'rnge_id' : 'RNGE_ID',
    'acres' : 'ACRES',
    'range_id' : 'RANGE_ID',
    'bnd_ft' : 'BND_FT',
    'draw' : 'DRAW',
    'shoshone' : 'SHOSHONE',
    'tranlattio' : 'TRANLATTIO',
    'bannock' : 'BANNOCK',
    'geom' : 'MULTIPOLYGON',
}

range_units_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'shbt', 'range_units.shp'))

def run(verbose=True):

    boundary_lm = LayerMapping(
        models.boundary, boundary_shp, boundary_mapping,
        transform=False, encoding='iso-8859-1'
    )
    boundary_lm.save(strict=True, verbose=verbose)

    districts_lm = LayerMapping(
        models.districts, districts_shp, districts_mapping,
        transform=False, encoding='iso-8859-1'
    )
    districts_lm.save(strict=True, verbose=verbose)

    ownership_lm = LayerMapping(
        models.ownership, ownership_shp, ownership_mapping,
        transform=False, encoding='iso-8859-1'
    )
    ownership_lm.save(strict=True, verbose=verbose)

    range_units_lm = LayerMapping(
        models.range_units, range_units_shp, range_units_mapping,
        transform=False, encoding='iso-8859-1'
    )
    range_units_lm.save(strict=True, verbose=verbose)
