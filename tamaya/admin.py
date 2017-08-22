from django.contrib import admin
from django.contrib.admin import AdminSite
from . import models

class tamayaAdmin(AdminSite):
    site_header = 'Santa Ana Pueblo Webmap Login'
    site_url = '/tamaya/'

tamaya_admin = tamayaAdmin(name='tamaya_admin')
tamaya_admin.register(models.Document)
