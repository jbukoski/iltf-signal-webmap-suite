from django.contrib.gis.db import models

class boundary(models.Model):
    aiannhce = models.CharField(max_length=4)
    aiannhns = models.CharField(max_length=8)
    affgeoid = models.CharField(max_length=13)
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
    objectid = models.BigIntegerField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class clco_parcels(models.Model):
    pnum = models.CharField(max_length=12)
    prop_id = models.BigIntegerField()
    acres_gis = models.FloatField()
    situs_addr = models.CharField(max_length=15)
    situs_dir = models.CharField(max_length=1)
    situs_rd = models.CharField(max_length=50)
    situs_ext = models.CharField(max_length=10)
    situs_city = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=5)
    pacs_link = models.CharField(max_length=127)
    pmt_link = models.CharField(max_length=127)
    tribal = models.CharField(max_length=10)
    ownership = models.CharField(max_length=30)
    jskt_statu = models.CharField(max_length=25)
    prev_owner = models.CharField(max_length=25)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class jefco_parcels(models.Model):
    pin = models.BigIntegerField()
    pin_string = models.CharField(max_length=80)
    prop_id = models.BigIntegerField()
    township = models.CharField(max_length=80)
    range = models.CharField(max_length=80)
    section_field = models.CharField(max_length=80)
    qtr_sectio = models.CharField(max_length=80)
    situs_addr = models.CharField(max_length=80)
    situs_city = models.CharField(max_length=80)
    situs_zip = models.CharField(max_length=80)
    owner = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    prev_own = models.CharField(max_length=40)
    acres = models.FloatField()
    tribal = models.CharField(max_length=10)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class jst_boundary_clco(models.Model):
    pnum = models.CharField(max_length=12)
    prop_id = models.BigIntegerField()
    acres_gis = models.FloatField()
    situs_addr = models.CharField(max_length=15)
    situs_dir = models.CharField(max_length=1)
    situs_rd = models.CharField(max_length=50)
    situs_ext = models.CharField(max_length=10)
    situs_city = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=5)
    pacs_link = models.CharField(max_length=127)
    pmt_link = models.CharField(max_length=127)
    tribal = models.CharField(max_length=10)
    ownership = models.CharField(max_length=30)
    jskt_statu = models.CharField(max_length=25)
    prev_owner = models.CharField(max_length=25)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class jst_boundary_jefco(models.Model):
    pin = models.BigIntegerField()
    pin_string = models.CharField(max_length=80)
    prop_id = models.BigIntegerField()
    township = models.CharField(max_length=80)
    range = models.CharField(max_length=80)
    section_field = models.CharField(max_length=80)
    qtr_sectio = models.CharField(max_length=80)
    situs_addr = models.CharField(max_length=80)
    situs_city = models.CharField(max_length=80)
    situs_zip = models.CharField(max_length=80)
    owner = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    prev_own = models.CharField(max_length=40)
    acres = models.FloatField()
    tribal = models.CharField(max_length=10)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class jst_fee_parcels_clco(models.Model):
    pnum = models.CharField(max_length=12)
    prop_id = models.BigIntegerField()
    acres_gis = models.FloatField()
    situs_addr = models.CharField(max_length=15)
    situs_dir = models.CharField(max_length=1)
    situs_rd = models.CharField(max_length=50)
    situs_ext = models.CharField(max_length=10)
    situs_city = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=5)
    pacs_link = models.CharField(max_length=127)
    pmt_link = models.CharField(max_length=127)
    tribal = models.CharField(max_length=10)
    ownership = models.CharField(max_length=30)
    jskt_statu = models.CharField(max_length=25)
    prev_owner = models.CharField(max_length=25)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class jst_land_consol_area(models.Model):
    fid_pttown = models.BigIntegerField()
    data = models.CharField(max_length=45)
    fid_servic = models.BigIntegerField()
    id = models.BigIntegerField()
    area = models.FloatField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class jst_reservation_parcels_clco(models.Model):
    pnum = models.CharField(max_length=12)
    prop_id = models.BigIntegerField()
    acres_gis = models.FloatField()
    situs_addr = models.CharField(max_length=15)
    situs_dir = models.CharField(max_length=1)
    situs_rd = models.CharField(max_length=50)
    situs_ext = models.CharField(max_length=10)
    situs_city = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=5)
    pacs_link = models.CharField(max_length=127)
    pmt_link = models.CharField(max_length=127)
    tribal = models.CharField(max_length=10)
    ownership = models.CharField(max_length=30)
    jskt_statu = models.CharField(max_length=25)
    prev_owner = models.CharField(max_length=25)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class jst_trust_parcels_clco(models.Model):
    pnum = models.CharField(max_length=12)
    prop_id = models.BigIntegerField()
    acres_gis = models.FloatField()
    situs_addr = models.CharField(max_length=15)
    situs_dir = models.CharField(max_length=1)
    situs_rd = models.CharField(max_length=50)
    situs_ext = models.CharField(max_length=10)
    situs_city = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=5)
    pacs_link = models.CharField(max_length=127)
    pmt_link = models.CharField(max_length=127)
    tribal = models.CharField(max_length=10)
    ownership = models.CharField(max_length=30)
    jskt_statu = models.CharField(max_length=25)
    prev_owner = models.CharField(max_length=25)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)



#####################
## For file upload ##
#####################

class Document(models.Model):
    name = models.CharField(max_length=40)
    docfile = models.FileField(upload_to='jskt/uploaded')
