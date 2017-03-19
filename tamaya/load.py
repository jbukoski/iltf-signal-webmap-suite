import os
from django.contrib.gis.utils import LayerMapping
from .models import boundary, mbls, roads, soil_data

# Admin mappings and shapefiles

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
    'rd_id' : 'ID__',
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

roads_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'reservation_roads.shp'))

# Soil layer mappings and shapefiles

soil_data_mapping = {
    'poly_id' : 'poly_id',
    'areasymbol' : 'AREASYMBOL',
    'spatialver' : 'SPATIALVER',
    'musym' : 'MUSYM',
    'mukey' : 'MUKEY',
    'mukey_1' : 'MUKEY_1',
    'tax_class' : 'tax_class',
    'org_matter' : 'org_matter',
    'composting' : 'composting',
    'texture' : 'texture',
    'ph_water' : 'ph_water',
    'bulk_densi' : 'bulk_densi',
    'geom' : 'POLYGON',
}

soil_data_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'tamaya_soil_data.shp'))

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

    soil_data_lm = LayerMapping(
        soil_data, soil_data_shp, soil_data_mapping,
        transform=False, encoding='iso-8859-1',
    )
    soil_data_lm.save(strict=True, verbose=verbose)
