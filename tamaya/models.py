from django.contrib.gis.db import models

# RASTER 

class landfire_evt(models.Model):
    raster_id = models.TextField(primary_key=True)
    name = models.TextField()
    raster = models.RasterField()

class ndviDiff(models.Model):
    raster_id = models.TextField(primary_key=True)
    name = models.TextField()
    raster = models.RasterField()

class forest_agc(models.Model):
    raster_id = models.TextField(primary_key=True)
    name = models.TextField()
    raster = models.RasterField()

class forest_bgc(models.Model):
    raster_id = models.TextField(primary_key=True)
    name = models.TextField()
    raster = models.RasterField()

# LANDFIRE EVT ATTRIBUTES

class landfire_classes(models.Model):
    value = models.FloatField()
    label = models.TextField()

# ADMIN LAYERS

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

class mbls(models.Model):
    mbls_id = models.AutoField(primary_key=True)
    area = models.FloatField()
    perimeter = models.FloatField()
    mbl_field = models.IntegerField()
    mbl_id = models.IntegerField()
    acres = models.FloatField()
    comment = models.CharField(max_length=80)

    geom = models.PolygonField(srid=4326)

    objects = models.GeoManager()

    class Meta:
        verbose_name_plural = 'Master Business Leases'

    def __str__(self):
        return '%s' % (self.comment)

# ROAD LAYERS

class roads(models.Model):
    roads_id = models.AutoField(primary_key=True)
    distance = models.FloatField()
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

# HYDROLOGY LAYERS

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

# SOIL LAYERS

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

###########################
## For file upload
###########################

class Document(models.Model):
    #docfile = models.FileField(upload_to='documents/')
    #docfile = models.FileField(upload_to='tamaya/sample_up')
    docfile = models.FileField(upload_to='tamaya/uploaded')
    #uploaded_time = models.DateTimeField(auto_now_add=True)
