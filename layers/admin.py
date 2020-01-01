from django.contrib import admin

from .models import Vlan, VlanSubnets, Subnet, Interface, IPAddress, Machine

class VlanSubnetsInline(admin.TabularInline):
    extra = 0
    model = VlanSubnets

@admin.register(Vlan)
class VlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'identifier', 'identifier2')
    inlines = (VlanSubnetsInline,)

@admin.register(Subnet)
class SubnetAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip_network')

class IPAddressInline(admin.TabularInline):
    extra = 0
    model = IPAddress

@admin.register(Interface)
class InterfaceAdmin(admin.ModelAdmin):
    list_display = ('mac_address', 'machine', 'owner')
    inlines = (IPAddressInline,)

class InterfaceInline(admin.TabularInline):
    extra = 0
    model = Interface

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')
    inlines = (InterfaceInline,)
