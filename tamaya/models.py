from django.contrib.gis.db import models

class boundary(models.Model):
    id = models.IntegerField(primary_key=True)
    area = models.FloatField()
    perimeter = models.FloatField()
    acres = models.FloatField()
    comments = models.CharField(max_length=80)

    geom = models.MultiPolygonField(srid=4326)

    objects = models.GeoManager()

    def __str__(self):
        return '%s' % (self.id)

class mbls(models.Model):
    area = models.FloatField()
    perimeter = models.FloatField()
    mbl_field = models.IntegerField()
    mbl_id = models.IntegerField()
    acres = models.FloatField()
    comment = models.CharField(primary_key=True, max_length=80)

    geom = models.PolygonField(srid=4326)

    objects = models.GeoManager()

    def __str__(self):
        return '%s' % (self.comment)

class roads(models.Model):
    id = models.AutoField(primary_key=True)
    length = models.FloatField()
    rd_id = models.IntegerField(default=9999)
    access = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    number = models.CharField(max_length=80)
    surface = models.CharField(max_length=80)
    condition = models.CharField(max_length=80)
    rd_class = models.FloatField()
    rd_type = models.CharField(max_length=80)
    sa_id = models.CharField(max_length=80)
    surf_type = models.CharField(max_length=80)
    status = models.CharField(max_length=80)
    hunting = models.CharField(max_length=80)
    comment = models.CharField(max_length=80)
    restrict = models.CharField(max_length=80)
    roadrepair = models.CharField(max_length=80)

    geom = models.MultiLineStringField(srid=4326)

    def __str__(self):
        return '%s' % (self.id)

class bulk_density(models.Model):
    areasymbol = models.CharField(max_length=20)
    spatialver = models.BigIntegerField()
    musym = models.CharField(max_length=6)
    mukey = models.CharField(max_length=30)
    mukey_1 = models.CharField(max_length=10)
    db3rdbar = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
