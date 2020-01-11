from django.contrib import admin

from .models import BuildingGroup, Building


class BuildingInline(admin.TabularInline):
    extra = 0
    model = Building

@admin.register(BuildingGroup)
class BuildingGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'full_name')
    inlines = (BuildingInline,)
