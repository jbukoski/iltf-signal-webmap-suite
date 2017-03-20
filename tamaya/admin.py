from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import boundary, mbls, roads, soil_data, user_pts, user_lines, user_polygons

class tamayaAdmin(AdminSite):
    site_header = 'Santa Ana Pueblo Administration'

tamaya_admin = tamayaAdmin(name='tamaya_admin')
tamaya_admin.register(boundary)
tamaya_admin.register(mbls)
tamaya_admin.register(roads)
tamaya_admin.register(soil_data)
tamaya_admin.register(user_pts)
tamaya_admin.register(user_lines)
tamaya_admin.register(user_polygons)
