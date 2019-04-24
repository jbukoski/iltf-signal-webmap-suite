from django.contrib.gis.db import models

class boundary(models.Model):
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


class buff_bndry(models.Model):
    id = models.BigIntegerField()
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
