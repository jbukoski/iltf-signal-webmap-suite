from django.contrib.gis.db import models

class ashland_cnty(models.Model):
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


class bayfield_cnty(models.Model):
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


class beachroute(models.Model):
    state_fips = models.CharField(max_length=2)
    county_fip = models.CharField(max_length=3)
    road_name = models.CharField(max_length=100)
    route_type = models.CharField(max_length=1)
    tiger_feat = models.CharField(max_length=5)
    shape_len = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class boundary(models.Model):
    dfirm_id = models.CharField(max_length=6)
    version_id = models.CharField(max_length=11)
    pol_ar_id = models.CharField(max_length=32)
    pol_name1 = models.CharField(max_length=50)
    pol_name2 = models.CharField(max_length=50)
    pol_name3 = models.CharField(max_length=50)
    co_fips = models.CharField(max_length=3)
    st_fips = models.CharField(max_length=2)
    comm_no = models.CharField(max_length=4)
    cid = models.CharField(max_length=6)
    ani_tf = models.CharField(max_length=1)
    ani_firm = models.CharField(max_length=6)
    com_nfo_id = models.CharField(max_length=32)
    source_cit = models.CharField(max_length=21)
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class buff_bndry(models.Model):
    id = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class claytoncreektrail(models.Model):
    type = models.CharField(max_length=10)
    tident = models.CharField(max_length=24)
    ident = models.CharField(max_length=24)
    latitude = models.FloatField()
    longitude = models.FloatField()
    y_proj = models.FloatField()
    x_proj = models.FloatField()
    comment = models.CharField(max_length=254)
    new_trk = models.CharField(max_length=10)
    new_seg = models.CharField(max_length=10)
    display = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    altitude = models.FloatField()
    depth = models.FloatField()
    temp = models.FloatField()
    time = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    filename = models.CharField(max_length=254)
    ltime = models.CharField(max_length=20)
    desc_field = models.CharField(max_length=254)
    link = models.CharField(max_length=254)
    geom = models.MultiLineStringField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class conservationmgmtarea(models.Model):
    id = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class easyroute(models.Model):
    state_fips = models.CharField(max_length=2)
    county_fip = models.CharField(max_length=3)
    road_name = models.CharField(max_length=100)
    route_type = models.CharField(max_length=1)
    tiger_feat = models.CharField(max_length=5)
    shape_len = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class fbtnp(models.Model):
    id = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class frogbaytrails(models.Model):
    id = models.IntegerField()
    length = models.FloatField()
    name = models.CharField(max_length=20)
    geom = models.MultiLineStringField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class rc_zoning_districts(models.Model):
    objectid = models.BigIntegerField()
    area = models.FloatField()
    rbd4_field = models.BigIntegerField()
    rbd4_id = models.BigIntegerField()
    rbd4_name = models.CharField(max_length=30)
    id = models.BigIntegerField()
    district = models.CharField(max_length=50)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class s_fld_haz_ar(models.Model):
    dfirm_id = models.CharField(max_length=6)
    version_id = models.CharField(max_length=11)
    fld_ar_id = models.CharField(max_length=32)
    study_typ = models.CharField(max_length=28)
    fld_zone = models.CharField(max_length=17)
    zone_subty = models.CharField(max_length=57)
    sfha_tf = models.CharField(max_length=1)
    static_bfe = models.FloatField()
    v_datum = models.CharField(max_length=17)
    depth = models.FloatField()
    len_unit = models.CharField(max_length=16)
    velocity = models.FloatField()
    vel_unit = models.CharField(max_length=20)
    ar_revert = models.CharField(max_length=17)
    ar_subtrv = models.CharField(max_length=57)
    bfe_revert = models.FloatField()
    dep_revert = models.FloatField()
    dual_zone = models.CharField(max_length=1)
    source_cit = models.CharField(max_length=21)
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class s_fld_haz_ln(models.Model):
    dfirm_id = models.CharField(max_length=6)
    version_id = models.CharField(max_length=11)
    fld_ln_id = models.CharField(max_length=32)
    ln_typ = models.CharField(max_length=26)
    source_cit = models.CharField(max_length=21)
    geom = models.MultiLineStringField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class s_trnsport_ln(models.Model):
    dfirm_id = models.CharField(max_length=6)
    version_id = models.CharField(max_length=11)
    trans_id = models.CharField(max_length=32)
    mtfcc = models.CharField(max_length=70)
    fullname = models.CharField(max_length=100)
    altname1 = models.CharField(max_length=100)
    altname2 = models.CharField(max_length=100)
    routenum = models.CharField(max_length=6)
    route_typ = models.CharField(max_length=14)
    source_cit = models.CharField(max_length=21)
    geom = models.MultiLineStringField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class s_wtr_ar(models.Model):
    dfirm_id = models.CharField(max_length=6)
    version_id = models.CharField(max_length=11)
    wtr_ar_id = models.CharField(max_length=32)
    wtr_nm = models.CharField(max_length=100)
    shown_firm = models.CharField(max_length=1)
    shown_indx = models.CharField(max_length=1)
    source_cit = models.CharField(max_length=21)
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class s_wtr_ln(models.Model):
    dfirm_id = models.CharField(max_length=6)
    version_id = models.CharField(max_length=11)
    wtr_ln_id = models.CharField(max_length=32)
    wtr_nm = models.CharField(max_length=100)
    shown_firm = models.CharField(max_length=1)
    shown_indx = models.CharField(max_length=1)
    source_cit = models.CharField(max_length=21)
    geom = models.MultiLineStringField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class watersheds(models.Model):
    objectid = models.BigIntegerField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    acres = models.FloatField()
    avg_slope = models.FloatField()
    watershed = models.CharField(max_length=20)
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)



#####################
## For file upload ##
#####################

class Document(models.Model):
    name = models.CharField(max_length=40)
    docfile = models.FileField(upload_to='rcbc/uploaded')
