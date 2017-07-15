from django.contrib import admin
from django.contrib.admin import AdminSite
from . import models

class tamayaAdmin(AdminSite):
    site_header = 'Santa Ana Pueblo Webmap Login'
    site_url = '/tamaya/'

tamaya_admin = tamayaAdmin(name='tamaya_admin')
tamaya_admin.register(models.boundary)
tamaya_admin.register(models.mbls)
tamaya_admin.register(models.roads)
tamaya_admin.register(models.soil_data)
tamaya_admin.register(models.Document)
