import os
from django.contrib.gis.utils import LayerMapping
from . import models

ashland_cnty_mapping = {
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

ashland_cnty_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'rcbc', 'ashland_cnty.shp'))

bayfield_cnty_mapping = {
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

bayfield_cnty_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'rcbc', 'bayfield_cnty.shp'))

boundary_mapping = {
    'area' : 'AREA',
    'perimeter' : 'PERIMETER',
    'rbd4_field' : 'RBD4_',
    'rbd4_id' : 'RBD4_ID',
    'rbd4_name' : 'RBD4_NAME',
    'acres' : 'ACRES',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

boundary_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'rcbc', 'boundary.shp'))

buff_bndry_mapping = {
    'id' : 'id',
    'geom' : 'MULTIPOLYGON',
}

buff_bndry_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'rcbc', 'buff_bndry.shp'))

claytoncreektrail_mapping = {
    'type' : 'type',
    'tident' : 'tident',
    'ident' : 'ident',
    'latitude' : 'Latitude',
    'longitude' : 'Longitude',
    'y_proj' : 'y_proj',
    'x_proj' : 'x_proj',
    'comment' : 'comment',
    'new_trk' : 'new_trk',
    'new_seg' : 'new_seg',
    'display' : 'display',
    'color' : 'color',
    'altitude' : 'altitude',
    'depth' : 'depth',
    'temp' : 'temp',
    'time' : 'time',
    'model' : 'model',
    'filename' : 'filename',
    'ltime' : 'ltime',
    'desc_field' : 'desc_',
    'link' : 'link',
    'geom' : 'MULTILINESTRING',
}

claytoncreektrail_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'rcbc', 'claytoncreektrail.shp'))

conservationmgmtarea_mapping = {
    'id' : 'Id',
    'geom' : 'MULTIPOLYGON',
}

conservationmgmtarea_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'rcbc', 'conservationmgmtarea.shp'))

fbtnp_mapping = {
    'id' : 'Id',
    'geom' : 'MULTIPOLYGON',
}

fbtnp_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'rcbc', 'fbtnp.shp'))

frog_bay_trails_mapping = {
    'state_fips' : 'STATE_FIPS',
    'county_fip' : 'COUNTY_FIP',
    'road_name' : 'ROAD_NAME',
    'route_type' : 'ROUTE_TYPE',
    'id' : 'Id',
    'length' : 'Length',
    'name' : 'Name',
    'geom' : 'MULTILINESTRING',
}

frog_bay_trails_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'rcbc', 'frog_bay_trails.shp'))

s_fld_haz_ar_mapping = {
    'dfirm_id' : 'DFIRM_ID',
    'version_id' : 'VERSION_ID',
    'fld_ar_id' : 'FLD_AR_ID',
    'study_typ' : 'STUDY_TYP',
    'fld_zone' : 'FLD_ZONE',
    'zone_subty' : 'ZONE_SUBTY',
    'sfha_tf' : 'SFHA_TF',
    'static_bfe' : 'STATIC_BFE',
    'v_datum' : 'V_DATUM',
    'depth' : 'DEPTH',
    'len_unit' : 'LEN_UNIT',
    'velocity' : 'VELOCITY',
    'vel_unit' : 'VEL_UNIT',
    'ar_revert' : 'AR_REVERT',
    'ar_subtrv' : 'AR_SUBTRV',
    'bfe_revert' : 'BFE_REVERT',
    'dep_revert' : 'DEP_REVERT',
    'dual_zone' : 'DUAL_ZONE',
    'source_cit' : 'SOURCE_CIT',
    'geom' : 'MULTIPOLYGON',
}

s_fld_haz_ar_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'rcbc', 's_fld_haz_ar.shp'))

s_fld_haz_ln_mapping = {
    'dfirm_id' : 'DFIRM_ID',
    'version_id' : 'VERSION_ID',
    'fld_ln_id' : 'FLD_LN_ID',
    'ln_typ' : 'LN_TYP',
    'source_cit' : 'SOURCE_CIT',
    'geom' : 'MULTILINESTRING',
}

s_fld_haz_ln_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'rcbc', 's_fld_haz_ln.shp'))

s_trnsport_ln_mapping = {
    'dfirm_id' : 'DFIRM_ID',
    'version_id' : 'VERSION_ID',
    'trans_id' : 'TRANS_ID',
    'mtfcc' : 'MTFCC',
    'fullname' : 'FULLNAME',
    'altname1' : 'ALTNAME1',
    'altname2' : 'ALTNAME2',
    'routenum' : 'ROUTENUM',
    'route_typ' : 'ROUTE_TYP',
    'source_cit' : 'SOURCE_CIT',
    'geom' : 'MULTILINESTRING',
}

s_trnsport_ln_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'rcbc', 's_trnsport_ln.shp'))

s_wtr_ar_mapping = {
    'dfirm_id' : 'DFIRM_ID',
    'version_id' : 'VERSION_ID',
    'wtr_ar_id' : 'WTR_AR_ID',
    'wtr_nm' : 'WTR_NM',
    'shown_firm' : 'SHOWN_FIRM',
    'shown_indx' : 'SHOWN_INDX',
    'source_cit' : 'SOURCE_CIT',
    'geom' : 'MULTIPOLYGON',
}

s_wtr_ar_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'rcbc', 's_wtr_ar.shp'))

s_wtr_ln_mapping = {
    'dfirm_id' : 'DFIRM_ID',
    'version_id' : 'VERSION_ID',
    'wtr_ln_id' : 'WTR_LN_ID',
    'wtr_nm' : 'WTR_NM',
    'shown_firm' : 'SHOWN_FIRM',
    'shown_indx' : 'SHOWN_INDX',
    'source_cit' : 'SOURCE_CIT',
    'geom' : 'MULTILINESTRING',
}

s_wtr_ln_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'rcbc', 's_wtr_ln.shp'))

watersheds_mapping = {
    'objectid' : 'OBJECTID',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'acres' : 'Acres',
    'avg_slope' : 'Avg_Slope',
    'watershed' : 'Watershed',
    'geom' : 'MULTIPOLYGON',
}

watersheds_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'rcbc', 'watersheds.shp'))

def run_new(verbose=True):

    frog_bay_trails_lm = LayerMapping(
        models.frog_bay_trails, frog_bay_trails_shp, frog_bay_trails_mapping,
        transform=False, encoding='iso-8859-1'
    )
    frog_bay_trails_lm.save(strict=True, verbose=verbose)


def run(verbose=True):

    ashland_cnty_lm = LayerMapping(
        models.ashland_cnty, ashland_cnty_shp, ashland_cnty_mapping,
        transform=False, encoding='iso-8859-1'
    )
    ashland_cnty_lm.save(strict=True, verbose=verbose)

    bayfield_cnty_lm = LayerMapping(
        models.bayfield_cnty, bayfield_cnty_shp, bayfield_cnty_mapping,
        transform=False, encoding='iso-8859-1'
    )
    bayfield_cnty_lm.save(strict=True, verbose=verbose)

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

    claytoncreektrail_lm = LayerMapping(
        models.claytoncreektrail, claytoncreektrail_shp, claytoncreektrail_mapping,
        transform=False, encoding='iso-8859-1'
    )
    claytoncreektrail_lm.save(strict=True, verbose=verbose)

    conservationmgmtarea_lm = LayerMapping(
        models.conservationmgmtarea, conservationmgmtarea_shp, conservationmgmtarea_mapping,
        transform=False, encoding='iso-8859-1'
    )
    conservationmgmtarea_lm.save(strict=True, verbose=verbose)

    fbtnp_lm = LayerMapping(
        models.fbtnp, fbtnp_shp, fbtnp_mapping,
        transform=False, encoding='iso-8859-1'
    )
    fbtnp_lm.save(strict=True, verbose=verbose)

    frog_bay_trails_lm = LayerMapping(
        models.frog_bay_trails, frog_bay_trails_shp, frog_bay_trails_mapping,
        transform=False, encoding='iso-8859-1'
    )
    frog_bay_trails_lm.save(strict=True, verbose=verbose)

    s_fld_haz_ar_lm = LayerMapping(
        models.s_fld_haz_ar, s_fld_haz_ar_shp, s_fld_haz_ar_mapping,
        transform=False, encoding='iso-8859-1'
    )
    s_fld_haz_ar_lm.save(strict=True, verbose=verbose)

    s_fld_haz_ln_lm = LayerMapping(
        models.s_fld_haz_ln, s_fld_haz_ln_shp, s_fld_haz_ln_mapping,
        transform=False, encoding='iso-8859-1'
    )
    s_fld_haz_ln_lm.save(strict=True, verbose=verbose)

    s_trnsport_ln_lm = LayerMapping(
        models.s_trnsport_ln, s_trnsport_ln_shp, s_trnsport_ln_mapping,
        transform=False, encoding='iso-8859-1'
    )
    s_trnsport_ln_lm.save(strict=True, verbose=verbose)

    s_wtr_ar_lm = LayerMapping(
        models.s_wtr_ar, s_wtr_ar_shp, s_wtr_ar_mapping,
        transform=False, encoding='iso-8859-1'
    )
    s_wtr_ar_lm.save(strict=True, verbose=verbose)

    s_wtr_ln_lm = LayerMapping(
        models.s_wtr_ln, s_wtr_ln_shp, s_wtr_ln_mapping,
        transform=False, encoding='iso-8859-1'
    )
    s_wtr_ln_lm.save(strict=True, verbose=verbose)

    watersheds_lm = LayerMapping(
        models.watersheds, watersheds_shp, watersheds_mapping,
        transform=False, encoding='iso-8859-1'
    )
    watersheds_lm.save(strict=True, verbose=verbose)
