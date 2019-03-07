from django.contrib import admin
from django.contrib.admin import AdminSite
from . import models

class bmicAdmin(AdminSite):
    site_header = 'Bay Mills Webmap Login'
    site_url = '/bmic/'

bmic_admin = bmicAdmin(name='bmic_admin')
#bmic_admin.register(models.Document)
