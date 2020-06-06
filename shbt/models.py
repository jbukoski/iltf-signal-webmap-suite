from django.contrib.gis.db import models

class boundary(models.Model):
    sec = models.CharField(max_length=50)
    t = models.CharField(max_length=50)
    r = models.CharField(max_length=50)
    poly_area = models.FloatField()
    area_geo = models.FloatField()
    perimeter = models.FloatField()
    perim_geo = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class buff_bndry(models.Model):
    fid = models.BigIntegerField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class districts(models.Model):
    total_ac = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class ownership(models.Model):
    area = models.FloatField()
    perimeter = models.FloatField()
    lstmoss_wg = models.BigIntegerField()
    lstmoss_1 = models.BigIntegerField()
    lstmoss_at = models.CharField(max_length=20)
    lease_a = models.CharField(max_length=10)
    original = models.CharField(max_length=25)
    status = models.CharField(max_length=5)
    lease_b = models.CharField(max_length=10)
    lease_c = models.CharField(max_length=10)
    key = models.CharField(max_length=35)
    recording_field = models.CharField(max_length=20)
    key2 = models.CharField(max_length=45)
    lease_d = models.CharField(max_length=10)
    rpd_num = models.CharField(max_length=254)
    tenant = models.CharField(max_length=254)
    section = models.CharField(max_length=254)
    township = models.CharField(max_length=254)
    range = models.CharField(max_length=254)
    lstatus = models.CharField(max_length=254)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    curr_own = models.CharField(max_length=254)
    tribal_int = models.FloatField()
    acreage = models.FloatField()
    res_code = models.CharField(max_length=50)
    trib_own_m = models.FloatField()
    trib_own_s = models.FloatField()
    poly_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class range_units(models.Model):
    area = models.FloatField()
    perimeter = models.FloatField()
    rnge_field = models.IntegerField()
    rnge_id = models.IntegerField()
    acres = models.FloatField()
    range_id = models.CharField(max_length=25)
    bnd_ft = models.FloatField()
    draw = models.IntegerField()
    shoshone = models.CharField(max_length=25)
    tranlattio = models.CharField(max_length=35)
    bannock = models.CharField(max_length=25)
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)



#####################
## For file upload ##
#####################

class Document(models.Model):
    name = models.CharField(max_length=40)
    docfile = models.FileField(upload_to='shbt/uploaded')
