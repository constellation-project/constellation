import ipaddress

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.indexes import Index
from django.utils.translation import gettext_lazy as _

from .layer2 import MACAddressField, Vlan
from .layer3 import Subnet


class SubnetVlans(models.Model):
    subnet = models.OneToOneField(Subnet, on_delete=models.CASCADE, related_name='vlans')
    vlans = models.ManyToManyField(Vlan)

class IPAddress(models.Model):
    subnet = models.ForeignKey(Subnet, on_delete=models.PROTECT)
    address = models.GenericIPAddressField(protocol='both', unique=True)
    interface = models.ForeignKey('Interface', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def clean(self):
        network = self.subnet.ip_network()
        if ipaddress.ip_address(self.address) not in network:
            raise ValidationError(_("IP address must be in {subnet}.").format(subnet=network))

class Machine(models.Model):
    name = models.CharField(
        unique=True,
        max_length=63,
        validators=[
            RegexValidator(r'[a-zA-Z0-9][a-zA-Z0-9-]{0,62}(?<!-)'),
        ],
    )
    owner = models.ForeignKey('auth.User', on_delete=models.PROTECT, related_name='machines')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [models.Index(fields=['owner'])]

class Interface(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='interfaces')
    mac_address = MACAddressField(unique=True)
    subnets = models.ManyToManyField(Subnet, related_name='+', through=IPAddress)

    def owner(self):
        return self.machine.owner

    def __str__(self):
        return "{mac_address}@{machine}".format(
            mac_address=self.mac_address,
            machine=self.machine
        )
