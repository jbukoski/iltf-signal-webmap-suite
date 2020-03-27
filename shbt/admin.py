from django.contrib import admin
from django.contrib.admin import AdminSite
from . import models

class shbtAdmin(AdminSite):
    site_header = 'CHANGE ME IN TRIBE/ADMIN.PY'
    site_url = '/shbt/'

shbt_admin = shbtAdmin(name='shbt_admin')
