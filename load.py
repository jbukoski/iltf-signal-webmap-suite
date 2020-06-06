import os
from django.contrib.gis.utils import LayerMapping
from . import models



*_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', '', '*.shp'))

def run(verbose=True):

    *_lm = LayerMapping(
        models.*, *_shp, *_mapping,
        transform=False, encoding='iso-8859-1'
    )
    *_lm.save(strict=True, verbose=verbose)
