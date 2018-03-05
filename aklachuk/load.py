import os
from django.contrib.gis.utils import LayerMapping
from . import models

boundary_mapping = {
    'objectid' : 'OBJECTID',
    'own_type' : 'own_type',
    'own_name' : 'own_name',
    'mgr_name_d' : 'mgr_name_d',
    'p_des_tp' : 'p_des_tp',
    'p_loc_ds' : 'p_loc_ds',
    'p_des_nm' : 'p_des_nm',
    'p_loc_nm' : 'p_loc_nm',
    's_des_tp' : 's_des_tp',
    's_loc_ds' : 's_loc_ds',
    's_des_nm' : 's_des_nm',
    's_loc_nm' : 's_loc_nm',
    't_des_tp' : 't_des_tp',
    't_loc_ds' : 't_loc_ds',
    't_des_nm' : 't_des_nm',
    't_loc_nm' : 't_loc_nm',
    'state_nm' : 'state_nm',
    'gap_sts' : 'gap_sts',
    'iucn_cat' : 'iucn_cat',
    'gis_src' : 'gis_src',
    'src_date' : 'src_date',
    'comments' : 'comments',
    'gis_acres' : 'gis_acres',
    'status' : 'status',
    'fia_code' : 'FIA_code',
    'shape_leng' : 'Shape_Leng',
    'res_status' : 'Res_status',
    'shape_le_1' : 'Shape_Le_1',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

boundary_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'aklachuk', 'boundary.shp'))

carbon_avoided_conversion_mapping = {
    'id' : 'Id',
    'mgmt_unit' : 'Mgmt_Unit',
    'yr_establi' : 'Yr_Establi',
    'acres' : 'Acres',
    'fid_1' : 'FID_1',
    'id_1' : 'Id_1',
    'mgmt_uni_1' : 'Mgmt_Uni_1',
    'yr_estab_1' : 'Yr_Estab_1',
    'sixteen_yr' : 'Sixteen_Yr',
    'land_type' : 'Land_Type',
    'threat' : 'Threat',
    'acres_1' : 'Acres_1',
    'nrcs_pract' : 'NRCS_Pract',
    'peracreco2' : 'PerAcreCO2',
    'peryrtonsc' : 'perYrTonsC',
    'tons_co2e_field' : 'Tons_CO2e_',
    'geom' : 'MULTIPOLYGON',
}

carbon_avoided_conversion_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'aklachuk', 'carbon_avoided_conversion.shp'))

carbon_food_plots_mapping = {
    'id' : 'Id',
    'mgmt_unit' : 'Mgmt_Unit',
    'yr_establi' : 'Yr_Establi',
    'acres' : 'Acres',
    'fid_1' : 'FID_1',
    'id_1' : 'Id_1',
    'mgmt_uni_1' : 'Mgmt_Uni_1',
    'yr_estab_1' : 'Yr_Estab_1',
    'land_type' : 'Land_Type',
    'duration' : 'Duration',
    'sixteen_ye' : 'Sixteen_ye',
    'acres_1' : 'Acres_1',
    'nrcs_pract' : 'NRCS_Pract',
    'per_acre_c' : 'Per_Acre_C',
    'per_year_t' : 'per_Year_T',
    'tons_co2e_field' : 'Tons_CO2e_',
    'sixteen__1' : 'Sixteen__1',
    'geom' : 'MULTIPOLYGON',
}

carbon_food_plots_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'aklachuk', 'carbon_food_plots.shp'))

carbon_native_grasslands_mapping = {
    'id' : 'Id',
    'mgmt_unit' : 'Mgmt_Unit',
    'yr_establi' : 'Yr_Establi',
    'acres' : 'Acres',
    'fid_1' : 'FID_1',
    'id_1' : 'Id_1',
    'mgmt_uni_1' : 'Mgmt_Uni_1',
    'land_type' : 'Land_Type',
    'yr_estab_1' : 'Yr_Estab_1',
    'acres_1' : 'Acres_1',
    'nrcs_pract' : 'NRCS_Pract',
    'peracreco2' : 'PerAcreCO2',
    'peryrtonsc' : 'perYrTonsC',
    'assumed_si' : 'Assumed_si',
    'geom' : 'MULTIPOLYGON',
}

carbon_native_grasslands_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'aklachuk', 'carbon_native_grasslands.shp'))

carbon_new_grasslands_mapping = {
    'id' : 'Id',
    'mgmt_unit' : 'Mgmt_Unit',
    'yr_establi' : 'Yr_Establi',
    'acres' : 'Acres',
    'fid_1' : 'FID_1',
    'id_1' : 'Id_1',
    'mgmt_uni_1' : 'Mgmt_Uni_1',
    'land_type' : 'Land_Type',
    'yr_estab_1' : 'Yr_Estab_1',
    'duration' : 'Duration',
    'sixteen_ye' : 'Sixteen_ye',
    'acres_1' : 'Acres_1',
    'nrcs_pract' : 'NRCS_Pract',
    'peracreco2' : 'PerAcreCO2',
    'peryrtonsc' : 'perYrTonsC',
    'tonssincec' : 'TonsSinceC',
    'sixteen__1' : 'Sixteen__1',
    'geom' : 'MULTIPOLYGON',
}

carbon_new_grasslands_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'aklachuk', 'carbon_new_grasslands.shp'))

carbon_new_treebelt_mapping = {
    'id' : 'Id',
    'mgmt_unit' : 'Mgmt_Unit',
    'yr_establi' : 'Yr_Establi',
    'acres' : 'Acres',
    'fid_1' : 'FID_1',
    'id_1' : 'Id_1',
    'mgmt_uni_1' : 'Mgmt_Uni_1',
    'yr_estab_1' : 'Yr_Estab_1',
    'duration' : 'Duration',
    'sixteen_ye' : 'Sixteen_ye',
    'acres_1' : 'Acres_1',
    'nrcs_pract' : 'NRCS_Pract',
    'per_acre_c' : 'Per_Acre_C',
    'per_yr_ton' : 'per_Yr_Ton',
    'tons_since' : 'Tons_Since',
    'sixteen__1' : 'Sixteen__1',
    'field13' : 'Field13',
    'geom' : 'MULTIPOLYGON',
}

carbon_new_treebelt_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'aklachuk', 'carbon_new_treebelt.shp'))

carbon_old_treebelts_mapping = {
    'id' : 'Id',
    'mgmt_unit' : 'Mgmt_Unit',
    'yr_establi' : 'Yr_Establi',
    'acres' : 'Acres',
    'fid_1' : 'FID_1',
    'id_1' : 'Id_1',
    'mgmt_uni_1' : 'Mgmt_Uni_1',
    'yr_estab_1' : 'Yr_Estab_1',
    'duration' : 'Duration',
    'sixteen_ye' : 'Sixteen_ye',
    'acres_1' : 'Acres_1',
    'nrcs_pract' : 'NRCS_Pract',
    'per_acre_c' : 'Per_Acre_C',
    'per_yr_ton' : 'per_Yr_Ton',
    'tons_since' : 'Tons_Since',
    'sixteen__1' : 'Sixteen__1',
    'field13' : 'Field13',
    'geom' : 'MULTIPOLYGON',
}

carbon_old_treebelts_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'aklachuk', 'carbon_old_treebelts.shp'))

carbon_wetlands_mapping = {
    'id' : 'Id',
    'mgmt_unit' : 'Mgmt_Unit',
    'yr_establi' : 'Yr_Establi',
    'acres' : 'Acres',
    'fid_1' : 'FID_1',
    'id_1' : 'Id_1',
    'mgmt_uni_1' : 'Mgmt_Uni_1',
    'yr_estab_1' : 'Yr_Estab_1',
    'duration' : 'Duration',
    'sixteen_ye' : 'Sixteen_ye',
    'acres_1' : 'Acres_1',
    'nrcs_pract' : 'NRCS_Pract',
    'per_acre_c' : 'Per_Acre_C',
    'per_yr_ton' : 'per_Yr_Ton',
    'tons_since' : 'Tons_Since',
    'sixteen__1' : 'Sixteen__1',
    'geom' : 'MULTIPOLYGON',
}

carbon_wetlands_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'aklachuk', 'carbon_wetlands.shp'))

cnties_bndry_mapping = {
    'statefp10' : 'STATEFP10',
    'countyfp10' : 'COUNTYFP10',
    'countyns10' : 'COUNTYNS10',
    'geoid10' : 'GEOID10',
    'name10' : 'NAME10',
    'namelsad10' : 'NAMELSAD10',
    'lsad10' : 'LSAD10',
    'classfp10' : 'CLASSFP10',
    'mtfcc10' : 'MTFCC10',
    'csafp10' : 'CSAFP10',
    'cbsafp10' : 'CBSAFP10',
    'metdivfp10' : 'METDIVFP10',
    'funcstat10' : 'FUNCSTAT10',
    'aland10' : 'ALAND10',
    'awater10' : 'AWATER10',
    'intptlat10' : 'INTPTLAT10',
    'intptlon10' : 'INTPTLON10',
    'intptlat' : 'INTPTLAT',
    'intptlon' : 'INTPTLON',
    'id' : 'ID',
    'id2' : 'ID2',
    'geo' : 'GEO',
    'target_geo' : 'TARGET_GEO',
    'target_g_1' : 'TARGET_G_1',
    'pop_total' : 'POP_TOTAL',
    'pop_hu' : 'POP_HU',
    'pop_occ_hu' : 'POP_OCC_HU',
    'pop_vac_hu' : 'POP_VAC_HU',
    'shape_area' : 'Shape_area',
    'shape_len' : 'Shape_len',
    'geom' : 'MULTIPOLYGON',
}

cnties_bndry_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'aklachuk', 'cnties_bndry.shp'))

counties_mapping = {
    'statefp10' : 'STATEFP10',
    'countyfp10' : 'COUNTYFP10',
    'countyns10' : 'COUNTYNS10',
    'geoid10' : 'GEOID10',
    'name10' : 'NAME10',
    'namelsad10' : 'NAMELSAD10',
    'lsad10' : 'LSAD10',
    'classfp10' : 'CLASSFP10',
    'mtfcc10' : 'MTFCC10',
    'csafp10' : 'CSAFP10',
    'cbsafp10' : 'CBSAFP10',
    'metdivfp10' : 'METDIVFP10',
    'funcstat10' : 'FUNCSTAT10',
    'aland10' : 'ALAND10',
    'awater10' : 'AWATER10',
    'intptlat10' : 'INTPTLAT10',
    'intptlon10' : 'INTPTLON10',
    'intptlat' : 'INTPTLAT',
    'intptlon' : 'INTPTLON',
    'id' : 'ID',
    'id2' : 'ID2',
    'geo' : 'GEO',
    'target_geo' : 'TARGET_GEO',
    'target_g_1' : 'TARGET_G_1',
    'pop_total' : 'POP_TOTAL',
    'pop_hu' : 'POP_HU',
    'pop_occ_hu' : 'POP_OCC_HU',
    'pop_vac_hu' : 'POP_VAC_HU',
    'shape_area' : 'Shape_area',
    'shape_len' : 'Shape_len',
    'geom' : 'MULTIPOLYGON',
}

counties_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'aklachuk', 'counties.shp'))

foodplots_mapping = {
    'objectid' : 'OBJECTID',
    'shape_leng' : 'SHAPE_Leng',
    'shape_area' : 'SHAPE_Area',
    'area' : 'AREA',
    'plot_numbe' : 'PLOT_NUMBE',
    'acres' : 'ACRES',
    'crop_2014' : 'CROP_2014',
    'crop_2015' : 'CROP_2015',
    'geom' : 'MULTIPOLYGON',
}

foodplots_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'aklachuk', 'foodplots.shp'))

grasslandsexport_mapping = {
    'operator' : 'OPERATOR',
    'program' : 'PROGRAM',
    'location' : 'LOCATION',
    'shape_area' : 'SHAPE_Area',
    'year_done' : 'YEAR_DONE',
    'acres' : 'ACRES',
    'cost' : 'COST',
    'geom' : 'MULTIPOLYGON',
}

grasslandsexport_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'aklachuk', 'grasslandsexport.shp'))

habitatleases_mapping = {
    'name' : 'NAME',
    'lease_or_p' : 'LEASE_OR_P',
    'start_date' : 'START_DATE',
    'end_date' : 'END_DATE',
    'annual_cos' : 'ANNUAL_COS',
    'total_acre' : 'TOTAL_ACRE',
    'payment_du' : 'PAYMENT_DU',
    'contract_l' : 'CONTRACT_L',
    'geom' : 'MULTIPOLYGON',
}

habitatleases_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'aklachuk', 'habitatleases.shp'))

homesiteshelterbelts_mapping = {
    'objectid' : 'OBJECTID',
    'operator' : 'OPERATOR',
    'program' : 'PROGRAM',
    'location' : 'LOCATION',
    'cost' : 'COST',
    'size_ac' : 'SIZE_AC',
    'number_of_field' : 'NUMBER_OF_',
    'year_done' : 'YEAR_DONE',
    'fabric_ft' : 'FABRIC_FT',
    'irrigated_field' : 'IRRIGATED_',
    'geom' : 'MULTIPOINT',
}

homesiteshelterbelts_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'aklachuk', 'homesiteshelterbelts.shp'))

new_purchases_mapping = {
    'objectid' : 'OBJECTID',
    'area' : 'AREA',
    'perimeter' : 'PERIMETER',
    'bigplsc_field' : 'BIGPLSC_',
    'bigplsc_id' : 'BIGPLSC_ID',
    'sec' : 'SEC',
    'town' : 'TOWN',
    'rng' : 'RNG',
    'mer' : 'MER',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'remarks' : 'remarks',
    'purch_name' : 'Purch_name',
    'purch_date' : 'Purch_date',
    'sect_t_r' : 'SECT_T_R',
    'legal_desc' : 'legal_desc',
    'acres_field' : 'ACRES_',
    'geom' : 'MULTIPOLYGON',
}

new_purchases_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'aklachuk', 'new_purchases.shp'))

parcels_mapping = {
    'area' : 'AREA',
    'perimeter' : 'PERIMETER',
    'biglst_field' : 'BIGLST_',
    'biglst_id' : 'BIGLST_ID',
    'pls_town' : 'PLS_TOWN',
    'pls_range' : 'PLS_RANGE',
    'pls_sec' : 'PLS_SEC',
    'pls_pm' : 'PLS_PM',
    'lst_owntyp' : 'LST_OWNTYP',
    'lst_restyp' : 'LST_RESTYP',
    'lst_open' : 'LST_OPEN',
    'lst_tractn' : 'LST_TRACTN',
    'lst_suffix' : 'LST_SUFFIX',
    'lst_mtract' : 'LST_MTRACT',
    'lst_msuffi' : 'LST_MSUFFI',
    'lst_lot' : 'LST_LOT',
    'lst_area' : 'LST_AREA',
    'lst_sym' : 'LST_SYM',
    'acres' : 'ACRES',
    'owntype' : 'OWNTYPE',
    'owner' : 'OWNER',
    'own' : 'OWN',
    'num' : 'NUM',
    'geom' : 'MULTIPOLYGON',
}

parcels_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'aklachuk', 'parcels.shp'))

trees_and_shrubs_mapping = {
    'operator' : 'OPERATOR',
    'program' : 'PROGRAM',
    'practice' : 'PRACTICE',
    'location' : 'LOCATION',
    'cost____field' : 'COST____',
    'size__ac_field' : 'SIZE__AC_',
    'z_of_trees' : 'Z_OF_TREES',
    'year_done' : 'YEAR_DONE',
    'fabric__ft' : 'FABRIC__FT',
    'irrigated' : 'IRRIGATED',
    'geom' : 'MULTIPOLYGON',
}

trees_and_shrubs_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'aklachuk', 'trees_and_shrubs.shp'))

wetlands_mapping = {
    'operator' : 'OPERATOR',
    'program' : 'PROGRAM',
    'practice' : 'PRACTICE',
    'location' : 'LOCATION',
    'cost____field' : 'COST____',
    'size__ac_field' : 'SIZE__AC_',
    'year_done' : 'YEAR_DONE',
    'geom' : 'MULTIPOINT',
}

wetlands_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'aklachuk', 'wetlands.shp'))

def run(verbose=True):

    boundary_lm = LayerMapping(
        aklachuk_boundary, boundary_shp, boundary_mapping,
        transform=False, encoding='iso-8859-1'
    )
    boundary_lm.save(strict=True, verbose=verbose)

    carbon_avoided_conversion_lm = LayerMapping(
        aklachuk_carbon_avoided_conversion, carbon_avoided_conversion_shp, carbon_avoided_conversion_mapping,
        transform=False, encoding='iso-8859-1'
    )
    carbon_avoided_conversion_lm.save(strict=True, verbose=verbose)

    carbon_food_plots_lm = LayerMapping(
        aklachuk_carbon_food_plots, carbon_food_plots_shp, carbon_food_plots_mapping,
        transform=False, encoding='iso-8859-1'
    )
    carbon_food_plots_lm.save(strict=True, verbose=verbose)

    carbon_native_grasslands_lm = LayerMapping(
        aklachuk_carbon_native_grasslands, carbon_native_grasslands_shp, carbon_native_grasslands_mapping,
        transform=False, encoding='iso-8859-1'
    )
    carbon_native_grasslands_lm.save(strict=True, verbose=verbose)

    carbon_new_grasslands_lm = LayerMapping(
        aklachuk_carbon_new_grasslands, carbon_new_grasslands_shp, carbon_new_grasslands_mapping,
        transform=False, encoding='iso-8859-1'
    )
    carbon_new_grasslands_lm.save(strict=True, verbose=verbose)

    carbon_new_treebelt_lm = LayerMapping(
        aklachuk_carbon_new_treebelt, carbon_new_treebelt_shp, carbon_new_treebelt_mapping,
        transform=False, encoding='iso-8859-1'
    )
    carbon_new_treebelt_lm.save(strict=True, verbose=verbose)

    carbon_old_treebelts_lm = LayerMapping(
        aklachuk_carbon_old_treebelts, carbon_old_treebelts_shp, carbon_old_treebelts_mapping,
        transform=False, encoding='iso-8859-1'
    )
    carbon_old_treebelts_lm.save(strict=True, verbose=verbose)

    carbon_wetlands_lm = LayerMapping(
        aklachuk_carbon_wetlands, carbon_wetlands_shp, carbon_wetlands_mapping,
        transform=False, encoding='iso-8859-1'
    )
    carbon_wetlands_lm.save(strict=True, verbose=verbose)

    cnties_bndry_lm = LayerMapping(
        aklachuk_cnties_bndry, cnties_bndry_shp, cnties_bndry_mapping,
        transform=False, encoding='iso-8859-1'
    )
    cnties_bndry_lm.save(strict=True, verbose=verbose)

    counties_lm = LayerMapping(
        aklachuk_counties, counties_shp, counties_mapping,
        transform=False, encoding='iso-8859-1'
    )
    counties_lm.save(strict=True, verbose=verbose)

    foodplots_lm = LayerMapping(
        aklachuk_foodplots, foodplots_shp, foodplots_mapping,
        transform=False, encoding='iso-8859-1'
    )
    foodplots_lm.save(strict=True, verbose=verbose)

    grasslandsexport_lm = LayerMapping(
        aklachuk_grasslandsexport, grasslandsexport_shp, grasslandsexport_mapping,
        transform=False, encoding='iso-8859-1'
    )
    grasslandsexport_lm.save(strict=True, verbose=verbose)

    habitatleases_lm = LayerMapping(
        aklachuk_habitatleases, habitatleases_shp, habitatleases_mapping,
        transform=False, encoding='iso-8859-1'
    )
    habitatleases_lm.save(strict=True, verbose=verbose)

    homesiteshelterbelts_lm = LayerMapping(
        aklachuk_homesiteshelterbelts, homesiteshelterbelts_shp, homesiteshelterbelts_mapping,
        transform=False, encoding='iso-8859-1'
    )
    homesiteshelterbelts_lm.save(strict=True, verbose=verbose)

    new_purchases_lm = LayerMapping(
        aklachuk_new_purchases, new_purchases_shp, new_purchases_mapping,
        transform=False, encoding='iso-8859-1'
    )
    new_purchases_lm.save(strict=True, verbose=verbose)

    parcels_lm = LayerMapping(
        aklachuk_parcels, parcels_shp, parcels_mapping,
        transform=False, encoding='iso-8859-1'
    )
    parcels_lm.save(strict=True, verbose=verbose)

    trees_and_shrubs_lm = LayerMapping(
        aklachuk_trees_and_shrubs, trees_and_shrubs_shp, trees_and_shrubs_mapping,
        transform=False, encoding='iso-8859-1'
    )
    trees_and_shrubs_lm.save(strict=True, verbose=verbose)

    wetlands_lm = LayerMapping(
        aklachuk_wetlands, wetlands_shp, wetlands_mapping,
        transform=False, encoding='iso-8859-1'
    )
    wetlands_lm.save(strict=True, verbose=verbose)
