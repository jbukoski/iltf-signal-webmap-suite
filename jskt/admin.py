from django.contrib import admin
from django.contrib.admin import AdminSite
from . import models

class jsktAdmin(AdminSite):
    site_header = 'CHANGE ME IN TRIBE/ADMIN.PY'
    site_url = '/jskt/'

jskt_admin = jsktAdmin(name='jskt_admin')
