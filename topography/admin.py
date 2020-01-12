from django.contrib import admin

from .models import BuildingGroup, Building, Room


class BuildingInline(admin.TabularInline):
    extra = 0
    model = Building

@admin.register(BuildingGroup)
class BuildingGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'full_name')
    inlines = (BuildingInline,)

class RoomInline(admin.TabularInline):
    extra = 0
    model = Room

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('number', 'group', 'name')
    inlines = (RoomInline,)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'building')
