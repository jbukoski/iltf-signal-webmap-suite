import os
from django.contrib.gis.utils import LayerMapping
from .models import boundary, mbls, roads, bulk_density

boundary_mapping = {
    'id' : 'Id',
    'area' : 'Area',
    'perimeter' : 'Perimeter',
    'acres' : 'Acres',
    'comments' : 'Comments',
    'geom' : 'MULTIPOLYGON',
}

boundary_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'boundary.shp'))

mbls_mapping = {
    'area' : 'AREA',
    'perimeter' : 'PERIMETER',
    'mbl_field' : 'MBL_',
    'mbl_id' : 'MBL_ID',
    'acres' : 'ACRES',
    'comment' : 'COMMENT',
    'geom' : 'POLYGON',
}

mbls_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'mbl_int.shp'))

roads_mapping = {
    'length' : 'LENGTH',
    'id' : 'ID__',
    'access' : 'ACCESS',
    'name' : 'NAME',
    'number' : 'NUMBER',
    'surface' : 'SURFACE',
    'condition' : 'CONDITION',
    'rd_class' : 'CLASS',
    'rd_type' : 'TYPE',
    'sa_id' : 'SA_ID',
    'surf_type' : 'Surf_Type',
    'status' : 'Status',
    'hunting' : 'Hunting',
    'comment' : 'Comment',
    'restrict' : 'Restrict',
    'roadrepair' : 'RoadRepair',
    'geom' : 'MULTILINESTRING',
}

bulk_density_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'bulk_density_1_3_bar.shp'))

bulk_density_mapping = {
    'areasymbol' : 'AREASYMBOL',
    'spatialver' : 'SPATIALVER',
    'musym' : 'MUSYM',
    'mukey' : 'MUKEY',
    'mukey_1' : 'MUKEY_1',
    'db3rdbar' : 'Db3rdbar',
    'geom' : 'MULTIPOLYGON',
}

roads_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'reservation_roads.shp'))

def run(verbose=True):

    boundary_lm = LayerMapping(
        boundary, boundary_shp, boundary_mapping,
        transform=False, encoding='iso-8859-1',
    )
    boundary_lm.save(strict=True, verbose=verbose)

    mbls_lm = LayerMapping(
        mbls, mbls_shp, mbls_mapping,
        transform=False, encoding='iso-8859-1',
    )
    mbls_lm.save(strict=True, verbose=verbose)

    roads_lm = LayerMapping(
        roads, roads_shp, roads_mapping,
        transform=False, encoding='iso-8859-1',
    )
    roads_lm.save(strict=True, verbose=verbose)

    bulk_density_lm = LayerMapping(
        bulk_density, bulk_density_shp, bulk_density_mapping,
        transform=False, encoding='iso-8859-1',
    )
    bulk_density_lm.save(strict=True, verbose=verbose)

