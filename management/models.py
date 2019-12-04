from django.db import models
from django.utils.translation import gettext_lazy as _


class ManagedInterface(models.Model):
    interface = models.OneToOneField('layers.Interface', related_name='domains', on_delete=models.PROTECT)
    a_records = models.ManyToManyField('dns.A', blank=True, related_name='+', verbose_name=_("A records"))
    aaaa_records = models.ManyToManyField('dns.AAAA', blank=True, related_name='+', verbose_name=_("AAAA records"))
    cname_records = models.ManyToManyField('dns.CNAME', blank=True, related_name='+', verbose_name=_("CNAME records"))
    ptr_records = models.ManyToManyField('dns.PTR', blank=True, related_name='+', verbose_name=_("PTR records"))
    firewall_layer2 = models.ManyToManyField('firewall.FireWallLayer2', , blank=True, related_name='+', verbose_name=_("Layer 2 firewalls"))
    firewall_layer3 = models.ManyToManyField('firewall.FireWallLayer3', , blank=True, related_name='+', verbose_name=_("Layer 3 firewalls"))
    firewall_layer4 = models.ManyToManyField('firewall.FireWallLayer4', , blank=True, related_name='+', verbose_name=_("Layer 4 firewalls"))
