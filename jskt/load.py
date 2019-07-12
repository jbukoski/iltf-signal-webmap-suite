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

boundary_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'jskt', 'boundary.shp'))

buff_bndry_mapping = {
    'objectid' : 'OBJECTID',
    'geom' : 'MULTIPOLYGON',
}

buff_bndry_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'jskt', 'buff_bndry.shp'))

clco_parcels_mapping = {
    'pnum' : 'PNUM',
    'prop_id' : 'PROP_ID',
    'acres_gis' : 'ACRES_GIS',
    'situs_addr' : 'SITUS_ADDR',
    'situs_dir' : 'SITUS_DIR',
    'situs_rd' : 'SITUS_RD',
    'situs_ext' : 'SITUS_EXT',
    'situs_city' : 'SITUS_CITY',
    'zip_code' : 'ZIP_CODE',
    'pacs_link' : 'PACS_LINK',
    'pmt_link' : 'PMT_LINK',
    'tribal' : 'Tribal',
    'ownership' : 'Ownership',
    'jskt_statu' : 'JSKT_statu',
    'prev_owner' : 'Prev_owner',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

clco_parcels_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'jskt', 'clco_parcels.shp'))

jefco_parcels_mapping = {
    'pin' : 'PIN',
    'pin_string' : 'PIN_STRING',
    'prop_id' : 'Prop_ID',
    'township' : 'Township',
    'range' : 'Range',
    'section_field' : 'Section_',
    'qtr_sectio' : 'Qtr_Sectio',
    'situs_addr' : 'Situs_Addr',
    'situs_city' : 'Situs_City',
    'situs_zip' : 'Situs_Zip',
    'owner' : 'Owner',
    'status' : 'Status',
    'prev_own' : 'Prev_own',
    'acres' : 'Acres',
    'tribal' : 'Tribal',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

jefco_parcels_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'jskt', 'jefco_parcels.shp'))

jst_boundary_clco_mapping = {
    'pnum' : 'PNUM',
    'prop_id' : 'PROP_ID',
    'acres_gis' : 'ACRES_GIS',
    'situs_addr' : 'SITUS_ADDR',
    'situs_dir' : 'SITUS_DIR',
    'situs_rd' : 'SITUS_RD',
    'situs_ext' : 'SITUS_EXT',
    'situs_city' : 'SITUS_CITY',
    'zip_code' : 'ZIP_CODE',
    'pacs_link' : 'PACS_LINK',
    'pmt_link' : 'PMT_LINK',
    'tribal' : 'Tribal',
    'ownership' : 'Ownership',
    'jskt_statu' : 'JSKT_statu',
    'prev_owner' : 'Prev_owner',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

jst_boundary_clco_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'jskt', 'jst_boundary_clco.shp'))

jst_boundary_jefco_mapping = {
    'pin' : 'PIN',
    'pin_string' : 'PIN_STRING',
    'prop_id' : 'Prop_ID',
    'township' : 'Township',
    'range' : 'Range',
    'section_field' : 'Section_',
    'qtr_sectio' : 'Qtr_Sectio',
    'situs_addr' : 'Situs_Addr',
    'situs_city' : 'Situs_City',
    'situs_zip' : 'Situs_Zip',
    'owner' : 'Owner',
    'status' : 'Status',
    'prev_own' : 'Prev_own',
    'acres' : 'Acres',
    'tribal' : 'Tribal',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

jst_boundary_jefco_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'jskt', 'jst_boundary_jefco.shp'))

jst_fee_parcels_clco_mapping = {
    'pnum' : 'PNUM',
    'prop_id' : 'PROP_ID',
    'acres_gis' : 'ACRES_GIS',
    'situs_addr' : 'SITUS_ADDR',
    'situs_dir' : 'SITUS_DIR',
    'situs_rd' : 'SITUS_RD',
    'situs_ext' : 'SITUS_EXT',
    'situs_city' : 'SITUS_CITY',
    'zip_code' : 'ZIP_CODE',
    'pacs_link' : 'PACS_LINK',
    'pmt_link' : 'PMT_LINK',
    'tribal' : 'Tribal',
    'ownership' : 'Ownership',
    'jskt_statu' : 'JSKT_statu',
    'prev_owner' : 'Prev_owner',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

jst_fee_parcels_clco_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'jskt', 'jst_fee_parcels_clco.shp'))

jst_land_consol_area_mapping = {
    'fid_pttown' : 'FID_pttown',
    'data' : 'DATA',
    'fid_servic' : 'FID_servic',
    'id' : 'ID',
    'area' : 'Area',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

jst_land_consol_area_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'jskt', 'jst_land_consol_area.shp'))

jst_reservation_parcels_clco_mapping = {
    'pnum' : 'PNUM',
    'prop_id' : 'PROP_ID',
    'acres_gis' : 'ACRES_GIS',
    'situs_addr' : 'SITUS_ADDR',
    'situs_dir' : 'SITUS_DIR',
    'situs_rd' : 'SITUS_RD',
    'situs_ext' : 'SITUS_EXT',
    'situs_city' : 'SITUS_CITY',
    'zip_code' : 'ZIP_CODE',
    'pacs_link' : 'PACS_LINK',
    'pmt_link' : 'PMT_LINK',
    'tribal' : 'Tribal',
    'ownership' : 'Ownership',
    'jskt_statu' : 'JSKT_statu',
    'prev_owner' : 'Prev_owner',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

jst_reservation_parcels_clco_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'jskt', 'jst_reservation_parcels_clco.shp'))

jst_trust_parcels_clco_mapping = {
    'pnum' : 'PNUM',
    'prop_id' : 'PROP_ID',
    'acres_gis' : 'ACRES_GIS',
    'situs_addr' : 'SITUS_ADDR',
    'situs_dir' : 'SITUS_DIR',
    'situs_rd' : 'SITUS_RD',
    'situs_ext' : 'SITUS_EXT',
    'situs_city' : 'SITUS_CITY',
    'zip_code' : 'ZIP_CODE',
    'pacs_link' : 'PACS_LINK',
    'pmt_link' : 'PMT_LINK',
    'tribal' : 'Tribal',
    'ownership' : 'Ownership',
    'jskt_statu' : 'JSKT_statu',
    'prev_owner' : 'Prev_owner',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

jst_trust_parcels_clco_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'jskt', 'jst_trust_parcels_clco.shp'))

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

    clco_parcels_lm = LayerMapping(
        models.clco_parcels, clco_parcels_shp, clco_parcels_mapping,
        transform=False, encoding='iso-8859-1'
    )
    clco_parcels_lm.save(strict=True, verbose=verbose)

    jefco_parcels_lm = LayerMapping(
        models.jefco_parcels, jefco_parcels_shp, jefco_parcels_mapping,
        transform=False, encoding='iso-8859-1'
    )
    jefco_parcels_lm.save(strict=True, verbose=verbose)

    jst_boundary_clco_lm = LayerMapping(
        models.jst_boundary_clco, jst_boundary_clco_shp, jst_boundary_clco_mapping,
        transform=False, encoding='iso-8859-1'
    )
    jst_boundary_clco_lm.save(strict=True, verbose=verbose)

    jst_boundary_jefco_lm = LayerMapping(
        models.jst_boundary_jefco, jst_boundary_jefco_shp, jst_boundary_jefco_mapping,
        transform=False, encoding='iso-8859-1'
    )
    jst_boundary_jefco_lm.save(strict=True, verbose=verbose)

    jst_fee_parcels_clco_lm = LayerMapping(
        models.jst_fee_parcels_clco, jst_fee_parcels_clco_shp, jst_fee_parcels_clco_mapping,
        transform=False, encoding='iso-8859-1'
    )
    jst_fee_parcels_clco_lm.save(strict=True, verbose=verbose)

    jst_land_consol_area_lm = LayerMapping(
        models.jst_land_consol_area, jst_land_consol_area_shp, jst_land_consol_area_mapping,
        transform=False, encoding='iso-8859-1'
    )
    jst_land_consol_area_lm.save(strict=True, verbose=verbose)

    jst_reservation_parcels_clco_lm = LayerMapping(
        models.jst_reservation_parcels_clco, jst_reservation_parcels_clco_shp, jst_reservation_parcels_clco_mapping,
        transform=False, encoding='iso-8859-1'
    )
    jst_reservation_parcels_clco_lm.save(strict=True, verbose=verbose)

    jst_trust_parcels_clco_lm = LayerMapping(
        models.jst_trust_parcels_clco, jst_trust_parcels_clco_shp, jst_trust_parcels_clco_mapping,
        transform=False, encoding='iso-8859-1'
    )
    jst_trust_parcels_clco_lm.save(strict=True, verbose=verbose)
