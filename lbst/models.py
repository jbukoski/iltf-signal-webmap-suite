from django.contrib.gis.db import models

# Admin Layers

class lbst_boundary(models.Model):
    boundary_id = models.AutoField(primary_key = True)
    objectid = models.BigIntegerField()
    own_type = models.CharField(max_length=254)
    own_name = models.CharField(max_length=254)
    mgr_name_d = models.CharField(max_length=254)
    p_des_tp = models.CharField(max_length=254)
    p_loc_ds = models.CharField(max_length=254)
    p_des_nm = models.CharField(max_length=254)
    p_loc_nm = models.CharField(max_length=254)
    s_des_tp = models.CharField(max_length=254)
    s_loc_ds = models.CharField(max_length=254)
    s_des_nm = models.CharField(max_length=254)
    s_loc_nm = models.CharField(max_length=254)
    t_des_tp = models.CharField(max_length=254)
    t_loc_ds = models.CharField(max_length=254)
    t_des_nm = models.CharField(max_length=254)
    t_loc_nm = models.CharField(max_length=254)
    state_nm = models.CharField(max_length=254)
    gap_sts = models.CharField(max_length=254)
    iucn_cat = models.CharField(max_length=254)
    gis_src = models.CharField(max_length=254)
    src_date = models.CharField(max_length=254)
    comments = models.CharField(max_length=254)
    gis_acres = models.FloatField()
    status = models.CharField(max_length=254)
    fia_code = models.CharField(max_length=254)
    shape_leng = models.FloatField()
    res_status = models.CharField(max_length=254)
    shape_le_1 = models.FloatField()
    shape_area = models.FloatField()

    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural = 'Reservation Boundary'

    def __str__(self):
        return '%s' % (self.boundary_id)

class lbst_parcels(models.Model):
    parcel_id = models.AutoField(primary_key=True)
    area = models.FloatField()
    perimeter = models.FloatField()
    biglst_field = models.FloatField()
    biglst_id = models.FloatField()
    pls_town = models.CharField(max_length=4)
    pls_range = models.CharField(max_length=4)
    pls_sec = models.CharField(max_length=2)
    pls_pm = models.CharField(max_length=2)
    lst_owntyp = models.CharField(max_length=1)
    lst_restyp = models.CharField(max_length=1)
    lst_open = models.CharField(max_length=2)
    lst_tractn = models.CharField(max_length=8)
    lst_suffix = models.CharField(max_length=3)
    lst_mtract = models.CharField(max_length=8)
    lst_msuffi = models.CharField(max_length=3)
    lst_lot = models.CharField(max_length=3)
    lst_area = models.FloatField()
    lst_sym = models.IntegerField()
    acres = models.BigIntegerField()
    owntype = models.FloatField()
    owner = models.FloatField()
    own = models.FloatField()
    num = models.FloatField()

    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural = 'Reservation Boundary'

    def __str__(self):
        return '%s' % (self.parcel_id)

class lbst_new_parcels(models.Model):
    new_parcel_id = models.AutoField(primary_key=True)
    objectid = models.BigIntegerField()
    area = models.FloatField()
    perimeter = models.FloatField()
    bigplsc_field = models.BigIntegerField()
    bigplsc_id = models.BigIntegerField()
    sec = models.IntegerField()
    town = models.CharField(max_length=3)
    rng = models.CharField(max_length=3)
    mer = models.IntegerField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    remarks = models.CharField(max_length=150)
    purch_name = models.CharField(max_length=50)
    purch_date = models.CharField(max_length=50)
    sect_t_r = models.CharField(max_length=50)
    legal_desc = models.CharField(max_length=250)
    acres_field = models.BigIntegerField()

    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural = 'Newly Acquired Parcels'

    def __str__(self):
        return '%s' % (self.new_parcel_id)

# Wildlife Habitat Layers

class food_plots(models.Model):
    food_plot_id = models.AutoField(primary_key = True)
    objectid = models.IntegerField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    area = models.CharField(max_length=50)
    plot_numbe = models.IntegerField()
    acres = models.FloatField()
    crop_2014 = models.CharField(max_length=50)
    crop_2015 = models.CharField(max_length=50)

    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural = 'Food Plots'

    def __str__(self):
        return '%s' % (self.food_plot_id)

class grasslands(models.Model):
    grasslands_id = models.AutoField(primary_key = True)
    operator = models.CharField(max_length=50)
    program = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    shape_area = models.FloatField()
    year_done = models.IntegerField()
    acres = models.FloatField()
    cost = models.IntegerField()

    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural = 'Grassland Exports'

    def __str__(self):
        return '%s' % (self.grasslands_id)


class habitat_leases(models.Model):
    lease_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    lease_or_p = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    annual_cos = models.IntegerField()
    total_acre = models.IntegerField()
    payment_du = models.CharField(max_length=50)
    contract_l = models.IntegerField()

    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural = 'Habitat Leases'

    def __str__(self):
        return '%s' % (self.name)

class shelterbelts(models.Model):
    shelterbelts_id = models.AutoField(primary_key = True)
    objectid = models.IntegerField()
    operator = models.CharField(max_length=50)
    program = models.CharField(max_length=50)
    location = models.CharField(max_length=25)
    cost = models.IntegerField()
    size_ac = models.FloatField()
    number_of_field = models.IntegerField()
    year_done = models.IntegerField()
    fabric_ft = models.IntegerField()
    irrigated_field = models.FloatField()

    geom = models.MultiPointField(srid=4326)

    class Meta:
        verbose_name_plural = 'Homesite Shelterbelts'

    def __str__(self):
        return '%s' % (self.shelterbelts_id)

class trees_shrubs(models.Model):
    trees_shrubs_id = models.AutoField(primary_key = True)
    operator = models.CharField(max_length=24)
    program = models.CharField(max_length=16)
    practice = models.CharField(max_length=20)
    location = models.CharField(max_length=16)
    cost_field = models.BigIntegerField()
    size_ac_field = models.FloatField()
    z_of_trees = models.BigIntegerField()
    year_done = models.BigIntegerField()
    fabric_ft = models.BigIntegerField()
    irrigated = models.CharField(max_length=10)

    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural = 'Trees and Shrubs'

    def __str__(self):
        return '%s' % (self.trees_shrubs_id)

class wetlands(models.Model):
    wetlands_id = models.AutoField(primary_key = True)
    operator = models.CharField(max_length=20)
    program = models.CharField(max_length=16)
    practice = models.CharField(max_length=20)
    location = models.CharField(max_length=16)
    cost_field = models.BigIntegerField()
    size_ac_field = models.FloatField()
    year_done = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural = 'Wetlands'

    def __str__(self):
        return '%s' % (self.wetlands_id)

# Carbon layers

class avoided_c(models.Model):
    avoided_c_id = models.AutoField(primary_key = True)
    feat_id = models.IntegerField()
    mgmt_unit = models.CharField(max_length=25)
    yr_establi = models.IntegerField()
    acres = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return '%s' % (self.avoided_c_id)

#####################
## For file upload ##
#####################

class document(models.Model):
    name = models.CharField(max_length=40)
    docfile = models.FileField(upload_to='lbst/uploaded')







