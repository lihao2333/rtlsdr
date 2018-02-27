from django.contrib import admin
from .models import Data
# Register your models here.
class DataAdmin(admin.ModelAdmin):
    list_display = ("owner", "loc_x", "loc_y", "fs", "fc", "agc", "psd", "time")
admin.site.register(Data, DataAdmin)
