from django.contrib import admin
from django.contrib.admin import AdminSite

class lbstAdmin(AdminSite):
    site_header = 'Lower Brule Sioux Tribe Admin Page'
    site_url = '/lbst/'

lbst_admin = lbstAdmin(name='lbst_admin')

