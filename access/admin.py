from django.contrib import admin

from .models import Switch, Port


class PortInline(admin.TabularInline):
    extra = 0
    model = Port

@admin.register(Switch)
class SwitchAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'building', 'location')
    inlines = (PortInline,)
