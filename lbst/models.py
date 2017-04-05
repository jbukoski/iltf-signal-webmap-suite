from django.contrib.gis.db import models

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
