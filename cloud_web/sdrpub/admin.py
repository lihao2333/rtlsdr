from django.contrib import admin
from .models import Sdr
# Register your models here.
class SdrAdmin(admin.ModelAdmin):
    list_display = ("name", "ip", "loc_x", "loc_y")
admin.site.register(Sdr, SdrAdmin)
