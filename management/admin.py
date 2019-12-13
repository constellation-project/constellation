from django.contrib import admin

from .models import ManagedInterface


@admin.register(ManagedInterface)
class ManagedInterfaceAdmin(admin.ModelAdmin):
    pass
