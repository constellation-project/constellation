from django.db import models
from polymorphic.models import PolymorphicModel

from layers.models import MACAddressField

class FireWallActionField(models.CharField):

    CHOICES = [
         ('ACCEPT', 'Accept'),
         (  'DROP', 'Drop'),
         ('REJECT', 'Reject')
    ]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 16
        kwargs['choices'] = FireWallActionField.CHOICES
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['max_length']
        del kwargs['choices']
        return name, path, args, kwargs

class FileWallLayer(PolymorphicModel):
    name = models.SlugField()
    out = models.NullBooleanField()
    action = FireWallActionField()

    class Meta:
        abstract = True

class FireWallLayer2(FileWallLayer):
    mac_address = MACAddressField()

class FireWallLayer3(FileWallLayer):
    prefix = models.GenericIPAddressField(protocol='both')
    length = models.PositiveSmallIntegerField()

class Layer4Protocol(models.Model):

    IP_PROTOCOLS = [
        (  1, 'ICMP'),
        (  6, 'TCP'),
        ( 17, 'UDP')
    ]

    protocol = models.PositiveSmallIntegerField(choices=IP_PROTOCOLS, unique=True)
    name = models.SlugField()

class FireWallLayer4(FileWallLayer):
    protocol = models.ForeignKey(Layer4Protocol, on_delete=models.PROTECT, related_name='+')
    port_start = models.PositiveIntegerField(null=True)
    port_end = models.PositiveIntegerField(null=True)

class FireWallRule(models.Model):
    name = models.SlugField()
    layer2 = models.ForeignKey(FireWallLayer2, null=True, on_delete=models.PROTECT, related_name='+')
    layer3 = models.ForeignKey(FireWallLayer3, null=True, on_delete=models.PROTECT, related_name='+')
    layer4 = models.ForeignKey(FireWallLayer4, null=True, on_delete=models.PROTECT, related_name='+')

class FireWall(models.Model):
    interface = models.OneToOneField('layers.Interface', on_delete=models.CASCADE, related_name='firewall')
    rules = models.ManyToManyField(FireWallRule)
