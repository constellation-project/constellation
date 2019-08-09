from django.contrib import admin

from .models import InterfaceDomains


@admin.register(InterfaceDomains)
class InterfaceDomainsAdmin(admin.ModelAdmin):
    pass
