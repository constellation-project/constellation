from rest_framework import viewsets

from .serializers import SubnetSerializer, VlanSerializer
from ..models import Subnet, Vlan


class SubnetViewSet(viewsets.ModelViewSet):
    queryset = Subnet.objects.all()
    serializer_class = SubnetSerializer

class VlanViewSet(viewsets.ModelViewSet):
    queryset = Vlan.objects.all()
    serializer_class = VlanSerializer
