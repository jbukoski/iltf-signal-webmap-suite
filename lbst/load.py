import os
from django.contrib.gis.utils import LayerMapping
from . import models

# Admin Layers

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

boundary_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'lbst', 'reservation_boundary.shp'))


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

parcels_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'lbst', 'parcels.shp'))

lbst_new_parcels_mapping = {
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

new_parcels_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'lbst', 'new_parcels.shp'))


# Wildlife Habitat Layers

food_plots_mapping = {
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

food_plots_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'lbst', 'food_plots.shp'))


grasslands_mapping = {
    'operator' : 'OPERATOR',
    'program' : 'PROGRAM',
    'location' : 'LOCATION',
    'shape_area' : 'SHAPE_Area',
    'year_done' : 'YEAR_DONE',
    'acres' : 'ACRES',
    'cost' : 'COST',
    'geom' : 'MULTIPOLYGON',
}

grasslands_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'lbst', 'grasslands_export.shp'))


habitat_leases_mapping = {
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

habitat_leases_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'lbst', 'HabitatLeases.shp'))


shelterbelts_mapping = {
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

shelterbelts_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'lbst', 'homesite_shelterbelts.shp'))


trees_shrubs_mapping = {
    'operator' : 'OPERATOR',
    'program' : 'PROGRAM',
    'practice' : 'PRACTICE',
    'location' : 'LOCATION',
    'cost_field' : 'COST____',
    'size_ac_field' : 'SIZE__AC_',
    'z_of_trees' : 'Z_OF_TREES',
    'year_done' : 'YEAR_DONE',
    'fabric_ft' : 'FABRIC__FT',
    'irrigated' : 'IRRIGATED',
    'geom' : 'MULTIPOLYGON',
}

trees_shrubs_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'lbst', 'trees_and_shrubs.shp'))


wetlands_mapping = {
    'operator' : 'OPERATOR',
    'program' : 'PROGRAM',
    'practice' : 'PRACTICE',
    'location' : 'LOCATION',
    'cost_field' : 'COST____',
    'size_ac_field' : 'SIZE__AC_',
    'year_done' : 'YEAR_DONE',
    'geom' : 'MULTIPOLYGON',
}

wetlands_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'lbst', 'wetlands.shp'))

# C layers

avoided_c_mapping = {
    'feat_id' : 'Id',
    'mgmt_unit' : 'Mgmt_Unit',
    'yr_establi' : 'Yr_Establi',
    'acres' : 'Acres',
    'geom' : 'MULTIPOLYGON',
}

avoided_c_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'lbst', 'avoided_c.shp'))

def load_bndry(verbose=True):
    boundary_lm = LayerMapping(
        models.boundary, boundary_shp, boundary_mapping,
        transform=False, encoding='iso-8859-1'
    )
    boundary_lm.save(strict=True, verbose=verbose)


def run(verbose=True):

    boundary_lm  = LayerMapping(
        lbst_boundary, boundary_shp, boundary_mapping,
        transform=False, encoding='iso-8859-1'
    )
    boundary_lm.save(strict=True, verbose=verbose)


    parcels_lm = LayerMapping(
        lbst_parcels, parcels_shp, parcels_mapping,
        transform=False, encoding='iso-8859-1'
    )
    parcels_lm.save(strict=True, verbose=verbose)


    new_parcels_lm = LayerMapping(
        lbst_new_parcels, new_parcels_shp, lbst_new_parcels_mapping,
        transform=False, encoding='iso-8859-1'
    )
    new_parcels_lm.save(strict=True, verbose=verbose)


    food_plots_lm = LayerMapping(
        food_plots, food_plots_shp, food_plots_mapping,
        transform=False, encoding='iso-8859-1'
    )
    food_plots_lm.save(strict=True, verbose=verbose)


    grasslands_lm = LayerMapping(
        grasslands, grasslands_shp, grasslands_mapping,
        transform=False, encoding='iso-8859-1'
    )
    grasslands_lm.save(strict=True, verbose=verbose)


    habitat_leases_lm = LayerMapping(
        habitat_leases, habitat_leases_shp, habitat_leases_mapping,
        transform=False, encoding='iso-8859-1',
    )
    habitat_leases_lm.save(strict=True, verbose=verbose)


    shelterbelts_lm = LayerMapping(
        shelterbelts, shelterbelts_shp, shelterbelts_mapping,
        transform=False, encoding='iso-8859-1',
    )
    shelterbelts_lm.save(strict=True, verbose=verbose)


    trees_shrubs_lm = LayerMapping(
        trees_shrubs, trees_shrubs_shp, trees_shrubs_mapping,
        transform=False, encoding='iso-8859-1',
    )
    trees_shrubs_lm.save(strict=True, verbose=verbose)

    wetlands_lm = LayerMapping(
        wetlands, wetlands_shp, wetlands_mapping,
        transform=False, encoding='iso-8859-1',
    )
    wetlands_lm.save(strict=True, verbose=verbose)

    avoided_c_lm = LayerMapping(
        models.avoided_c, avoided_c_shp, avoided_c_mapping,
        transform=False, encoding='iso-8859-1',
    )
    avoided_c_lm.save(strict=True, verbose=verbose)
