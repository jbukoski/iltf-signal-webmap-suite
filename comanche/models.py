from django.contrib.gis.db import models
from django.contrib.gis import geos

class cotton(models.Model):
    parcelid = models.CharField(max_length=34)
    ag_acres = models.FloatField()
    asd_acres = models.FloatField()
    agparcelid = models.CharField(max_length=25)
    parcelid_1 = models.CharField(max_length=254)
    owner = models.CharField(max_length=254)
    addr1 = models.CharField(max_length=254)
    addr2 = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    st = models.CharField(max_length=254)
    zip = models.CharField(max_length=254)
    school = models.BigIntegerField()
    acres = models.FloatField()
    ownerperc = models.FloatField()
    mktland = models.BigIntegerField()
    assdland = models.BigIntegerField()
    mktimp = models.BigIntegerField()
    assdimp = models.BigIntegerField()
    mktother = models.BigIntegerField()
    assdother = models.BigIntegerField()
    exemption = models.BigIntegerField()
    dblexempt = models.BigIntegerField()
    image = models.CharField(max_length=254)
    legal = models.CharField(max_length=254)

    geom = models.GeometryField(srid=-1)

    objects = models.GeoManager()

    def __str__(self):
        return '%s' % (self.parcelid)

## TODO: Added the below function to account for polygon/multipolygon features in
## the cotton model. The data currently won't load into a database. Try to
## fix, but also try to get other data into a model.
## https://gis.stackexchange.com/questions/13498/
##     can-polygons-be-generalized-to-multipolygons-in-geodjango

    def save(self, *args, **kwargs):
        # if geom ends up as a Polgon, make it into a MultiPolygon
        if self.geom and isinstance(self.geom, geos.Polygon):
            self.geom = geos.MultiPolygon(self.geom)
            self.save(*args, **kwargs)
