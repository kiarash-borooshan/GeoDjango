from django.contrib import admin
from .models import WorldBorder
# Register your models here.


@admin.register(WorldBorder)
class admin_decor(admin.ModelAdmin):
    list_display = ("name", )
