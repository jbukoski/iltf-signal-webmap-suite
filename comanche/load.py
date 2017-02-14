import os
from django.contrib.gis.utils import LayerMapping
from .models import cotton

cotton_mapping = {
    'parcelid' : 'PARCELID',
    'ag_acres' : 'ag_acres',
    'asd_acres' : 'asd_acres',
    'agparcelid' : 'AGPARCELID',
    'parcelid_1' : 'ParcelID_1',
    'owner' : 'Owner',
    'addr1' : 'Addr1',
    'addr2' : 'Addr2',
    'city' : 'City',
    'st' : 'St',
    'zip' : 'Zip',
    'school' : 'School',
    'acres' : 'Acres',
    'ownerperc' : 'OwnerPerc',
    'mktland' : 'MktLand',
    'assdland' : 'AssdLand',
    'mktimp' : 'MktImp',
    'assdimp' : 'AssdImp',
    'mktother' : 'MktOther',
    'assdother' : 'AssdOther',
    'exemption' : 'Exemption',
    'dblexempt' : 'DblExempt',
    'image' : 'Image',
    'legal' : 'Legal',
    'geom' : 'POLYGON',
}

cotton_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Parcels_Cotton_County_4326.shp'))

def run(verbose=True):

    cotton_lm = LayerMapping(
        cotton, cotton_shp, cotton_mapping,
        transform = False, encoding = 'iso-8859-1',
    )
    cotton_lm.save(strict=True, verbose=verbose)



