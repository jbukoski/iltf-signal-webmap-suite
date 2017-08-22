from django.contrib.gis.db import models

# Admin Layers

class boundary(models.Model):
    boundary_id = models.AutoField(primary_key=True)
    id = models.IntegerField()
    area = models.FloatField()
    perimeter = models.FloatField()
    acres = models.FloatField()
    comments = models.CharField(max_length=80)

    geom = models.MultiPolygonField(srid=4326)

    objects = models.GeoManager()

    class Meta:
        verbose_name_plural = 'Boundary'

    def __str__(self):
        return '%s' % (self.id)

class buffered_bndry(models.Model):
    dn = models.BigIntegerField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return '%s' % (self.dn)

class ag(models.Model):
    area = models.FloatField()
    perimeter = models.FloatField()
    acres = models.FloatField()
    use = models.CharField(max_length=254)
    service = models.CharField(max_length=254)
    ag_id = models.FloatField()
    status = models.CharField(max_length=254)
    group = models.CharField(max_length=254)
    owner = models.CharField(max_length=254)
    dissolve = models.BigIntegerField()
    tract_numb = models.CharField(max_length=254)
    ownership = models.CharField(max_length=254)
    community = models.CharField(max_length=254)
    soc_count = models.FloatField()
    soc_sum = models.FloatField()
    soc_mean = models.FloatField()
    soctotal = models.FloatField()
    socmean = models.FloatField()

    geom = models.MultiPolygonField(srid=4326)

    objects = models.GeoManager()

    def __str__(self):
        return '%s' % (self.ag_id)

class vineyards(models.Model):
    vineyard_id = models.BigIntegerField()
    acres = models.FloatField()
    section = models.CharField(max_length=254)
    soc_count = models.FloatField()
    soc_sum = models.FloatField()
    soc_mean = models.FloatField()
    soc_min = models.FloatField()
    soc_max = models.FloatField()
    soctotal = models.FloatField()
    socmean = models.FloatField()

    geom = models.MultiPolygonField(srid=4326)

    objects = models.GeoManager()

    def __str__(self):
        return '%s' % (self.vineyard_id)

class mbls(models.Model):
    area = models.FloatField()
    perimeter = models.FloatField()
    mbl_field = models.BigIntegerField()
    mbl_id = models.BigIntegerField()
    acres = models.FloatField()
    entity = models.CharField(max_length=254)
    outboundsp = models.FloatField()
    outbound_1 = models.FloatField()
    comment = models.CharField(max_length=254)
    boundary_m = models.BigIntegerField()
    boundary_1 = models.BigIntegerField()
    lotid = models.CharField(max_length=254)
    santa_ana = models.CharField(max_length=254)
    owner = models.CharField(max_length=254)
    acres_txt = models.CharField(max_length=254)
    dissolve = models.BigIntegerField()
    entity2 = models.CharField(max_length=254)
    soc_count = models.FloatField()
    soc_sum = models.FloatField()
    soc_mean = models.FloatField()
    soc_min = models.FloatField()
    soc_max = models.FloatField()
    soctotal = models.FloatField()
    socmean = models.FloatField()

    geom = models.PolygonField(srid=4326)

    objects = models.GeoManager()

    class Meta:
        verbose_name_plural = 'Master Business Leases'

    def __str__(self):
        return '%s' % (self.comment)

class roads(models.Model):
    roads_id = models.AutoField(primary_key=True)
    length = models.FloatField()
    id_field = models.BigIntegerField()
    access = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    number = models.CharField(max_length=254)
    surface = models.CharField(max_length=254)
    condition = models.CharField(max_length=254)
    road_class = models.FloatField(max_length=254)
    road_type = models.CharField(max_length=254)
    sa_id = models.CharField(max_length=254)
    surf_type = models.CharField(max_length=254)
    status = models.CharField(max_length=254)
    hunting = models.CharField(max_length=254)
    comment = models.CharField(max_length=254)
    restrict = models.CharField(max_length=254)
    roadrepair = models.BigIntegerField()
    geom = models.MultiLineStringField(srid=4326)

    class Meta:
        verbose_name_plural = 'Reservation Roads'

    def __str__(self):
        return '%s' % (self.roads_id)

# Hydrology Layers

class watersheds(models.Model):
    watershed_id = models.AutoField(primary_key=True)
    objectid = models.BigIntegerField()
    source = models.BigIntegerField()
    huc_8 = models.CharField(max_length=8)
    hu_8_name = models.CharField(max_length=80)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural = 'Watersheds'

    def __str__(self):
        return '%s' % (self.watershed_id)

class subwatersheds(models.Model):
    subwatershed_id = models.AutoField(primary_key=True)
    id = models.BigIntegerField()
    watershed = models.CharField(max_length=50)
    subwatshed = models.IntegerField()
    wsno = models.CharField(max_length=50)
    acres = models.FloatField()
    aveslope = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural = 'Subwatersheds'

    def __str__(self):
        return '%s' % (self.subwatershed_id)

class surfacehydro(models.Model):
    surfacehydro_id = models.AutoField(primary_key=True)
    id = models.BigIntegerField()
    geom = models.MultiLineStringField(srid=4326)

    class Meta:
        verbose_name_plural = 'Surface hydrology'

    def __str__(self):
        return '%s' % (self.surfacehydro_id)

# Soil Layers

class soil_data(models.Model):
    poly_id = models.BigIntegerField()
    areasymbol = models.CharField(max_length=20)
    spatialver = models.BigIntegerField()
    musym = models.CharField(max_length=6)
    mukey = models.CharField(max_length=30)
    mukey_1 = models.CharField(max_length=10)
    tax_class = models.CharField(max_length=254)
    org_matter = models.FloatField()
    composting = models.CharField(max_length=254)
    texture = models.CharField(max_length=254)
    ph_water = models.FloatField()
    bulk_densi = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    objects = models.GeoManager()

    class Meta:
        verbose_name_plural = 'Soil Data'

    def __str__(self):
        return '%s' % (self.poly_id)

# Vegetation Layers

class landfire_evt(models.Model):
    rast = models.RasterField()

class landfire_classes(models.Model):
    value = models.FloatField()
    label = models.TextField()

class ndvi_2005(models.Model):
    rast = models.RasterField()

class ndvi_2010(models.Model):
    rast = models.RasterField()

class ndvi_2015(models.Model):
    rast = models.RasterField()

# Carbon layers

class forest_agc(models.Model):
    rast = models.RasterField()

class forest_bgc(models.Model):
    rast = models.RasterField()

class gssurgo_soc(models.Model):
    rast = models.RasterField()

###########################
## For file upload
###########################

class Document(models.Model):
    name = models.CharField(max_length=40)
    docfile = models.FileField(upload_to='tamaya/uploaded')
