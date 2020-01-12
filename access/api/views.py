from rest_framework import viewsets

from .serializers import SwitchSerializer
from ..models import Switch


class SwitchViewSet(viewsets.ModelViewSet):
    queryset = Switch.objects.all()
    serializer_class = SwitchSerializer
    lookup_field = 'name'
