from django.contrib import admin
from .models import Branches, District
# Register your models here.


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(District, DistrictAdmin)


class BranchAdmin(admin.ModelAdmin):
    list_display = ['branchName', 'Tdistrict']
    prepopulated_fields = {'slug': ('branchName',)}


admin.site.register(Branches, BranchAdmin)
