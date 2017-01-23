from django.contrib import admin
from .models import boundary, mbls, roads

admin.site.register(boundary)
admin.site.register(mbls)
admin.site.register(roads)

