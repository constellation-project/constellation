import ipaddress

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.indexes import Index
from django.utils.translation import gettext_lazy as _

from .layer2 import MACAddressField, Vlan
from .layer3 import Subnet


class VlanSubnets(models.Model):
    vlan = models.OneToOneField(
        Vlan,
        on_delete=models.CASCADE,
        related_name='subnets',
        verbose_name=_("vlan"),
    )
    subnets = models.ManyToManyField(
        Subnet,
        verbose_name=_("IP subnet"),
    )

class IPAddress(models.Model):
    subnet = models.ForeignKey(
        Subnet,
        on_delete=models.PROTECT,
        verbose_name=_("IP subnet"),
    )
    address = models.GenericIPAddressField(
        protocol='both',
        unique=True,
        verbose_name=_("IP address"),
    )
    interface = models.ForeignKey(
        'Interface',
        on_delete=models.CASCADE,
        verbose_name=_("interface")
    )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def clean(self):
        network = self.subnet.ip_network()
        if ipaddress.ip_address(self.address) not in network:
            raise ValidationError(_("IP address must be in {subnet}.").format(subnet=network))

    def __str__(self):
        return f"{self.address}/{self.subnet.length}"

class Machine(models.Model):
    name = models.SlugField(
        unique=True,
        verbose_name=_("name"),
    )
    owner = models.ForeignKey(
        'auth.User',
        on_delete=models.PROTECT,
        related_name='machines',
        verbose_name=_("owner"),
    )
    description = models.TextField(
        blank=True,
        verbose_name=_("description"),
    )

    def __str__(self):
        return self.name

    class Meta:
        indexes = [models.Index(fields=['owner'])]

class Interface(models.Model):
    machine = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        related_name='interfaces',
        verbose_name=_("machine"),
    )
    mac_address = MACAddressField(
        unique=True,
        verbose_name=_("MAC address"),
    )
    subnets = models.ManyToManyField(
        Subnet,
        related_name='+',
        through=IPAddress,
        verbose_name=_("subnets")
    )

    def owner(self):
        return self.machine.owner

    def __str__(self):
        return "{mac_address}@{machine}".format(
            mac_address=self.mac_address,
            machine=self.machine
        )
