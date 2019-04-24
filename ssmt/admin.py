from django.contrib import admin
from django.contrib.admin import AdminSite
from . import models

class ssmtAdmin(AdminSite):
    site_header = 'Sioux St. Marie Tribe Webmap Login'
    site_url = '/ssmt/'

ssmt_admin = ssmtAdmin(name='ssmt_admin')
#ssmt_admin.register(models.Document)
