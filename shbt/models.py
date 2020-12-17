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


class counties(models.Model):
    objectid = models.BigIntegerField()
    name = models.CharField(max_length=32)
    state_name = models.CharField(max_length=35)
    state_fips = models.CharField(max_length=2)
    cnty_fips = models.CharField(max_length=3)
    fips = models.CharField(max_length=5)
    population = models.BigIntegerField()
    pop_sqmi = models.FloatField()
    pop2010 = models.BigIntegerField()
    pop10_sqmi = models.FloatField()
    white = models.BigIntegerField()
    black = models.BigIntegerField()
    ameri_es = models.BigIntegerField()
    asian = models.BigIntegerField()
    hawn_pi = models.BigIntegerField()
    hispanic = models.BigIntegerField()
    other = models.BigIntegerField()
    mult_race = models.BigIntegerField()
    males = models.BigIntegerField()
    females = models.BigIntegerField()
    age_under5 = models.BigIntegerField()
    age_5_9 = models.BigIntegerField()
    age_10_14 = models.BigIntegerField()
    age_15_19 = models.BigIntegerField()
    age_20_24 = models.BigIntegerField()
    age_25_34 = models.BigIntegerField()
    age_35_44 = models.BigIntegerField()
    age_45_54 = models.BigIntegerField()
    age_55_64 = models.BigIntegerField()
    age_65_74 = models.BigIntegerField()
    age_75_84 = models.BigIntegerField()
    age_85_up = models.BigIntegerField()
    med_age = models.FloatField()
    med_age_m = models.FloatField()
    med_age_f = models.FloatField()
    households = models.BigIntegerField()
    ave_hh_sz = models.FloatField()
    hsehld_1_m = models.BigIntegerField()
    hsehld_1_f = models.BigIntegerField()
    marhh_chd = models.BigIntegerField()
    marhh_no_c = models.BigIntegerField()
    mhh_child = models.BigIntegerField()
    fhh_child = models.BigIntegerField()
    families = models.BigIntegerField()
    ave_fam_sz = models.FloatField()
    hse_units = models.BigIntegerField()
    vacant = models.BigIntegerField()
    owner_occ = models.BigIntegerField()
    renter_occ = models.BigIntegerField()
    no_farms12 = models.FloatField()
    ave_size12 = models.FloatField()
    crop_acr12 = models.FloatField()
    ave_sale12 = models.FloatField()
    sqmi = models.FloatField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
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


class existing_wm(models.Model):
    name = models.CharField(max_length=60)
    geom = models.MultiLineStringField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class lagoon(models.Model):
    name = models.CharField(max_length=60)
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class lift_stations(models.Model):
    name = models.CharField(max_length=60)
    geom = models.MultiPointField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class nsi_flowlines(models.Model):
    comid = models.IntegerField()
    fdate = models.DateField()
    resolution = models.CharField(max_length=7)
    gnis_id = models.CharField(max_length=10)
    gnis_name = models.CharField(max_length=65)
    lengthkm = models.FloatField()
    reachcode = models.CharField(max_length=14)
    flowdir = models.CharField(max_length=15)
    ftype = models.CharField(max_length=24)
    fcode = models.IntegerField()
    areasqkm = models.FloatField()
    totdasqkm = models.FloatField()
    dup_comid = models.IntegerField()
    dup_arsqkm = models.FloatField()
    dup_length = models.FloatField()
    layer = models.CharField(max_length=100)
    path = models.CharField(max_length=254)
    geom = models.MultiLineStringField(srid=4326)
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


class pumphouses(models.Model):
    name = models.CharField(max_length=60)
    storage = models.IntegerField()
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


class res_soils(models.Model):
    areasymbol = models.CharField(max_length=80)
    spatialver = models.FloatField()
    musym = models.CharField(max_length=80)
    mukey = models.CharField(max_length=80)
    mu_name = models.CharField(max_length=143)
    farm_class = models.CharField(max_length=133)
    drainage = models.CharField(max_length=80)
    geomorph = models.CharField(max_length=80)
    taxonomy = models.CharField(max_length=89)
    soil_order = models.CharField(max_length=80, null = True)
    suborder = models.CharField(max_length=80, null = True)
    grt_group = models.CharField(max_length=80, null = True)
    moisture = models.CharField(max_length=80, null = True)
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class sewage_lines(models.Model):
    fnode_field = models.IntegerField()
    tnode_field = models.IntegerField()
    lpoly_field = models.IntegerField()
    rpoly_field = models.IntegerField()
    length = models.FloatField()
    sewer_field = models.IntegerField()
    sewer_id = models.IntegerField()
    desc_field = models.CharField(max_length=15)
    geom = models.MultiLineStringField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class storage_tanks(models.Model):
    name = models.CharField(max_length=60)
    geom = models.MultiPointField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)



#####################
## For file upload ##
#####################

class Document(models.Model):
    name = models.CharField(max_length=40)
    docfile = models.FileField(upload_to='shbt/uploaded')
