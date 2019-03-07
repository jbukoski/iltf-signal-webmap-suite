from django.apps import apps
from django.contrib import admin

mods = apps.all_models['bmic']

for i in mods.keys():
    print(i)

