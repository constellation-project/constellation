from django.db import models
from layers.models import Interface, Machine


class WifiInterface(Interface):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

class AccessPoint(Machine):
    location = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

class Switch(Machine):
    building = models.ForeignKey('topography.Building', on_delete=models.PROTECT)
    location = models.CharField(max_length=255)
    model = models.CharField(max_length=32)

class Port(models.Model):
    switch = models.ForeignKey(Switch, on_delete=models.CASCADE, related_name='ports')
    module = models.CharField(max_length=16, blank=True)
    number = models.PositiveSmallIntegerField()
    vlans = models.ManyToManyField('layers.Vlan')
    room = models.ForeignKey('topography.Room', null=True, blank=True, on_delete=models.SET_NULL, related_name='switch_ports')
    port = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    interface = models.ForeignKey('layers.Interface', null=True, blank=True, on_delete=models.SET_NULL, related_name='switch_port')

    def __str__(self):
        return f"{self.module}{self.number}@{self.switch.name}"

    class Meta:
        unique_together = ('switch', 'module', 'number')
