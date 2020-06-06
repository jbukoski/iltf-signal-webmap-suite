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

buff_bndry_mapping = {
    'fid' : 'FID',
    'geom' : 'MULTIPOLYGON',
}

buff_bndry_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'shbt', 'buff_bndry.shp'))

counties_mapping = {
    'objectid' : 'OBJECTID',
    'name' : 'NAME',
    'state_name' : 'STATE_NAME',
    'state_fips' : 'STATE_FIPS',
    'cnty_fips' : 'CNTY_FIPS',
    'fips' : 'FIPS',
    'population' : 'POPULATION',
    'pop_sqmi' : 'POP_SQMI',
    'pop2010' : 'POP2010',
    'pop10_sqmi' : 'POP10_SQMI',
    'white' : 'WHITE',
    'black' : 'BLACK',
    'ameri_es' : 'AMERI_ES',
    'asian' : 'ASIAN',
    'hawn_pi' : 'HAWN_PI',
    'hispanic' : 'HISPANIC',
    'other' : 'OTHER',
    'mult_race' : 'MULT_RACE',
    'males' : 'MALES',
    'females' : 'FEMALES',
    'age_under5' : 'AGE_UNDER5',
    'age_5_9' : 'AGE_5_9',
    'age_10_14' : 'AGE_10_14',
    'age_15_19' : 'AGE_15_19',
    'age_20_24' : 'AGE_20_24',
    'age_25_34' : 'AGE_25_34',
    'age_35_44' : 'AGE_35_44',
    'age_45_54' : 'AGE_45_54',
    'age_55_64' : 'AGE_55_64',
    'age_65_74' : 'AGE_65_74',
    'age_75_84' : 'AGE_75_84',
    'age_85_up' : 'AGE_85_UP',
    'med_age' : 'MED_AGE',
    'med_age_m' : 'MED_AGE_M',
    'med_age_f' : 'MED_AGE_F',
    'households' : 'HOUSEHOLDS',
    'ave_hh_sz' : 'AVE_HH_SZ',
    'hsehld_1_m' : 'HSEHLD_1_M',
    'hsehld_1_f' : 'HSEHLD_1_F',
    'marhh_chd' : 'MARHH_CHD',
    'marhh_no_c' : 'MARHH_NO_C',
    'mhh_child' : 'MHH_CHILD',
    'fhh_child' : 'FHH_CHILD',
    'families' : 'FAMILIES',
    'ave_fam_sz' : 'AVE_FAM_SZ',
    'hse_units' : 'HSE_UNITS',
    'vacant' : 'VACANT',
    'owner_occ' : 'OWNER_OCC',
    'renter_occ' : 'RENTER_OCC',
    'no_farms12' : 'NO_FARMS12',
    'ave_size12' : 'AVE_SIZE12',
    'crop_acr12' : 'CROP_ACR12',
    'ave_sale12' : 'AVE_SALE12',
    'sqmi' : 'SQMI',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

counties_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'shbt', 'counties.shp'))

districts_mapping = {
    'total_ac' : 'Total_Ac',
    'name' : 'Name',
    'geom' : 'MULTIPOLYGON',
}

districts_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'shbt', 'districts.shp'))

nsi_flowlines_mapping = {
    'comid' : 'ComID',
    'fdate' : 'FDate',
    'resolution' : 'RESOLUTION',
    'gnis_id' : 'GNIS_ID',
    'gnis_name' : 'GNIS_Name',
    'lengthkm' : 'LengthKM',
    'reachcode' : 'ReachCode',
    'flowdir' : 'FLOWDIR',
    'ftype' : 'FTYPE',
    'fcode' : 'FCode',
    'areasqkm' : 'AreaSqKM',
    'totdasqkm' : 'TotDASqKM',
    'dup_comid' : 'DUP_COMID',
    'dup_arsqkm' : 'DUP_ArSqKM',
    'dup_length' : 'DUP_Length',
    'layer' : 'layer',
    'path' : 'path',
    'geom' : 'MULTILINESTRING',
}

nsi_flowlines_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'shbt', 'nsi_flowlines.shp'))

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

def run_dos(verbose=True):

    counties_lm = LayerMapping(
        models.counties, counties_shp, counties_mapping,
        transform=False, encoding='iso-8859-1'
    )
    counties_lm.save(strict=True, verbose=verbose)

    nsi_flowlines_lm = LayerMapping(
        models.nsi_flowlines, nsi_flowlines_shp, nsi_flowlines_mapping,
        transform=False, encoding='iso-8859-1'
    )
    nsi_flowlines_lm.save(strict=True, verbose=verbose)



def run(verbose=True):

    boundary_lm = LayerMapping(
        models.boundary, boundary_shp, boundary_mapping,
        transform=False, encoding='iso-8859-1'
    )
    boundary_lm.save(strict=True, verbose=verbose)

    buff_bndry_lm = LayerMapping(
        models.buff_bndry, buff_bndry_shp, buff_bndry_mapping,
        transform=False, encoding='iso-8859-1'
    )
    buff_bndry_lm.save(strict=True, verbose=verbose)

    counties_lm = LayerMapping(
        models.counties, counties_shp, counties_mapping,
        transform=False, encoding='iso-8859-1'
    )
    counties_lm.save(strict=True, verbose=verbose)

    districts_lm = LayerMapping(
        models.districts, districts_shp, districts_mapping,
        transform=False, encoding='iso-8859-1'
    )
    districts_lm.save(strict=True, verbose=verbose)

    nsi_flowlines_lm = LayerMapping(
        models.nsi_flowlines, nsi_flowlines_shp, nsi_flowlines_mapping,
        transform=False, encoding='iso-8859-1'
    )
    nsi_flowlines_lm.save(strict=True, verbose=verbose)

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
