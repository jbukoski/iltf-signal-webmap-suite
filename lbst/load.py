import os
from django.contrib.gis.utils import LayerMapping
from .models import food_plots, grasslands, habitat_leases, shelterbelts, trees_shrubs, wetlands

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


def run(verbose=True):

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
