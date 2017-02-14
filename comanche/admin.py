from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import counties, cotton, caddo

class comancheAdmin(AdminSite):
    site_header = 'Comanche Administration'

comanche_admin = comancheAdmin(name='comanche_admin')
comanche_admin.register(counties)
comanche_admin.register(cotton)


