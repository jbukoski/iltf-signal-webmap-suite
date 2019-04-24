import os
from django.contrib.gis.utils import LayerMapping
from . import models

boundary_mapping = {
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

boundary_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'ssmt', 'boundary.shp'))

buff_bndry_mapping = {
    'id' : 'id',
    'geom' : 'MULTIPOLYGON',
}

buff_bndry_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'ssmt', 'buff_bndry.shp'))

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
