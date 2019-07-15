import os
from django.contrib.gis.utils import LayerMapping
from . import models

boundary_mapping = {
    'aiannhce' : 'AIANNHCE',
    'aiannhns' : 'AIANNHNS',
    'affgeoid' : 'AFFGEOID',
    'geoid' : 'GEOID',
    'name' : 'NAME',
    'lsad' : 'LSAD',
    'aland' : 'ALAND',
    'awater' : 'AWATER',
    'geom' : 'MULTIPOLYGON',
}

boundary_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'ssmt', 'boundary.shp'))

buff_bndry_mapping = {
    'id' : 'id',
    'geom' : 'MULTIPOLYGON',
}

buff_bndry_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'ssmt', 'buff_bndry.shp'))

ceded_territories_mapping = {
    'label' : 'LABEL',
    'treaty' : 'TREATY',
    'disputed' : 'DISPUTED',
    'website_la' : 'WEBSITE_LA',
    'geom' : 'MULTIPOLYGON25D',
}

ceded_territories_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'ssmt', 'ceded_territories.shp'))

parcels_mapping = {
    'objectid' : 'OBJECTID',
    'joined' : 'Joined',
    'planid' : 'PlanID',
    'name' : 'Name',
    'type' : 'Type',
    'statedarea' : 'StatedArea',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'category' : 'Category',
    'address' : 'Address',
    'city' : 'City',
    'wateracces' : 'WaterAcces',
    'zip' : 'Zip',
    'geom' : 'MULTIPOLYGON25D',
}

parcels_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'ssmt', 'parcels.shp'))

tax_areas_mapping = {
    'county' : 'County',
    'shape_leng' : 'SHAPE_Leng',
    'shape_area' : 'SHAPE_Area',
    'state' : 'State',
    'name' : 'Name',
    'geom' : 'MULTIPOLYGON',
}

tax_areas_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'ssmt', 'tax_areas.shp'))

units_mapping = {
    'id' : 'Id',
    'geom' : 'MULTIPOLYGON',
}

units_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'ssmt', 'units.shp'))

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

    ceded_territories_lm = LayerMapping(
        models.ceded_territories, ceded_territories_shp, ceded_territories_mapping,
        transform=False, encoding='iso-8859-1'
    )
    ceded_territories_lm.save(strict=True, verbose=verbose)

    parcels_lm = LayerMapping(
        models.parcels, parcels_shp, parcels_mapping,
        transform=False, encoding='iso-8859-1'
    )
    parcels_lm.save(strict=True, verbose=verbose)

    tax_areas_lm = LayerMapping(
        models.tax_areas, tax_areas_shp, tax_areas_mapping,
        transform=False, encoding='iso-8859-1'
    )
    tax_areas_lm.save(strict=True, verbose=verbose)

    units_lm = LayerMapping(
        models.units, units_shp, units_mapping,
        transform=False, encoding='iso-8859-1'
    )
    units_lm.save(strict=True, verbose=verbose)
