from django.contrib.gis.db import models

# Raster models

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

