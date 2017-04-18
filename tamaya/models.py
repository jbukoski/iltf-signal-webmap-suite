from django.contrib.gis.db import models

# Admin layers

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

class roads(models.Model):
    roads_id = models.AutoField(primary_key=True)
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

    class Meta:
        verbose_name_plural = 'Reservation Roads'

    def __str__(self):
        return '%s' % (self.roads_id)

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

# User-defined layers

class user_pts(models.Model):
    point_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    comment = models.CharField(max_length=100)
    geom = models.MultiPointField(srid=4326)

    objects = models.GeoManager()

    class Meta:
        verbose_name_plural = 'User-defined Points'

    def __str__(self):
        return '%s' % (self.point_id)

class user_lines(models.Model):
    line_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    comment = models.CharField(max_length=100)
    geom = models.MultiLineStringField(srid=4326)

    objects = models.GeoManager()

    class Meta:
        verbose_name_plural = 'User-defined Lines'

    def __str__(self):
        return '%s' % (self.line_id)

class user_polygons(models.Model):
    polygon_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    comment = models.CharField(max_length=100)
    geom = models.MultiPolygonField(srid=4326)

    objects = models.GeoManager()

    class Meta:
        verbose_name_plural = 'User-defined Polygons'

    def __str__(self):
        return '%s' % (self.polygon_id)
