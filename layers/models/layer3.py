import ipaddress

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class Subnet(models.Model):
    name = models.SlugField(unique=True)
    prefix = models.GenericIPAddressField(
        protocol='both',
        verbose_name=_("prefix")
    )
    length = models.PositiveSmallIntegerField(
        verbose_name=_("length")
    )

    def ip_network(self):
        return ipaddress.ip_network('{prefix}/{length}'.format(prefix=self.prefix, length=self.length))

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def clean(self):
        try:
            self.ip_network()
        except ValueError:
            raise ValidationError(_("Invalid IP subnet."))

    class Meta:
        unique_together = ('prefix', 'length')
