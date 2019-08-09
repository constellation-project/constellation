from django.core.exceptions import ValidationError
from django.db import models
from django import forms
from django.utils.translation import gettext_lazy as _


class MACAddressField(models.Field):

    def get_internal_type(self):
        return 'BigIntegerField'

    def to_python(self, value):
        if isinstance(value, str):
            return value
        elif isinstance(value, int):
            string = '{:012X}'.format(value)
            return ':'.join(string[i:i+2] for i in range(0, 12, 2))

    def from_db_value(self, value, expression, connection):
        return self.to_python(value)

    def get_prep_value(self, value):
        try:
            return int(value.replace(':', ''), 16)
        except:
            raise ValidationError(_("Invalid MAC address."))

    def formfield(self, **kwargs):
        if 'form_class' not in kwargs:
            kwargs['form_class'] = forms.CharField
        return super().formfield(**kwargs)


class Vlan(models.Model):
    name = models.SlugField()
    identifier = models.PositiveSmallIntegerField()
    identifier2 = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return "{name} {identifier}".format(
            name=self.name,
            identifier=(self.identifier, self.identifier2) if self.identifier2 else self.identifier
        )

    class Meta:
        unique_together = ('identifier', 'identifier2')
