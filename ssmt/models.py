from django.contrib.gis.db import models

class boundary(models.Model):
    aiannhce = models.CharField(max_length=4)
    aiannhns = models.CharField(max_length=8)
    affgeoid = models.CharField(null=True, max_length=13)
    geoid = models.CharField(max_length=4)
    name = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    aland = models.BigIntegerField()
    awater = models.BigIntegerField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class buff_bndry(models.Model):
    id = models.BigIntegerField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class parcels(models.Model):
    objectid = models.IntegerField()
    joined = models.IntegerField()
    planid = models.IntegerField()
    name = models.CharField(max_length=50)
    type = models.IntegerField()
    statedarea = models.CharField(max_length=50)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    category = models.CharField(max_length=50)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    wateracces = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class tax_areas(models.Model):
    county = models.CharField(max_length=50)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    state = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class units(models.Model):
    id = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)



#####################
## For file upload ##
#####################

class Document(models.Model):
    name = models.CharField(max_length=40)
    docfile = models.FileField(upload_to='ssmt/uploaded')
