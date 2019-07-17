from django.contrib import admin
from django.contrib.admin import AdminSite
from . import models

class rcbcAdmin(AdminSite):
    site_header = 'Red Cliff Band of the Lake Superior Chippewa'
    site_url = '/rcbc/'

rcbc_admin = rcbcAdmin(name='rcbc_admin')
