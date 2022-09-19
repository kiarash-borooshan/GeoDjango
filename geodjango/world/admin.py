# from django.contrib import admin
from .models import WorldBorder
from django.contrib.gis import admin


# Register your models here.

@admin.register(WorldBorder)
class admin_decor(admin.ModelAdmin):
    list_display = ("name", )
# class admin_decore(admin.GeoModelAdmin):
#     list_display = ("name",)
# class admin_decore(admin.GeoModelAdmin):
#         list_display = ("name",)
