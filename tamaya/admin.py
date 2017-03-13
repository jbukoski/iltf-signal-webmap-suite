from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import boundary, mbls, roads, user_pts

class tamayaAdmin(AdminSite):
    site_header = 'Santa Ana Pueblo Administration'

tamaya_admin = tamayaAdmin(name='tamaya_admin')
tamaya_admin.register(boundary)
tamaya_admin.register(mbls)
tamaya_admin.register(roads)
tamaya_admin.register(user_pts)
