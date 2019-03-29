from django.contrib import admin
from django.contrib.admin import AdminSite
from . import models

class RENAMEAdmin(AdminSite):
    site_header = 'CHANGE ME IN TRIBE/ADMIN.PY'
    site_url = '/RENAME/'

RENAME_admin = RENAMEAdmin(name='RENAME_admin')
