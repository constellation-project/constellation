from rest_framework import viewsets

from .serializers import InterfaceSerializer, MachineSerializer, \
    SubnetSerializer, VlanSerializer
from ..models import Interface, Machine, Subnet, Vlan


class InterfaceViewSet(viewsets.ModelViewSet):
    queryset = Interface.objects.all()
    serializer_class = InterfaceSerializer

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    lookup_field = 'name'

class SubnetViewSet(viewsets.ModelViewSet):
    queryset = Subnet.objects.all()
    serializer_class = SubnetSerializer
    lookup_field = 'name'

class VlanViewSet(viewsets.ModelViewSet):
    queryset = Vlan.objects.all()
    serializer_class = VlanSerializer
    lookup_field = 'name'
